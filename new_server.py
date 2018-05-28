import multiprocessing
from threading import Thread
from user import User
from game_room import *
import socket
from test import *

class Server:
    #创建主套接字
    @staticmethod
    def __main_socket(host,port):
        addr = (host,port)
        sockfd = socket.socket()
        sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sockfd.bind(addr)
        sockfd.listen(100)
        return sockfd

    #初始化服务器
    def __init__(self,host,port,pool):
        self.recvUserOutMsg,self.sendUserOutMsg=multiprocessing.Pipe()
        self.__host=host
        self.__port=port
        self.__sockfd=self.__main_socket(host,port)
        self.pool=pool
        self.game_num = {x: {'Users': [], 'Process': None,'UserExit':self.sendUserOutMsg,'Communication':multiprocessing.Pipe(False)} for x in range(pool)}
        self.__addr=(host,port)
        


    #创建新的线程来处理新连接
    def newThread(self,connfd):
        t=Thread(target=self.handler,args=(connfd,))
        t.setDaemon(True)
        t.start()

    #开始服务器处理新加入的连接
    def serve_forever(self):
        t=Thread(target=self.gameCommand)
        t1=Thread(target=self.clearGameDesk)
        t.setDaemon(True)
        t1.setDaemon(True)
        t.start()
        t1.start()
        while True:
            connfd, addr = self.__sockfd.accept()
            self.newThread(connfd)

    #处理客户请求
    def handler(self,connfd):
        userInfo = User(connfd)
        data =eval(userInfo.getMessage().decode())
        if data['title'] == 'register':
            userInfo.register(data['data'])   #注册用户
        elif data['title'] == 'login':
            userInfo.setUserPwd(userInfo.splitUserPwd(data['data'])) 
            self.login(userInfo)#登录游戏
        else:
            userInfo.closeSockfd()

    #退出游戏时清理该桌的信息
    def clearGameDesk(self):
        while True:
            user = self.recvUserOutMsg.recv()
            for i in self.game_num:
                if user in self.game_num[i]['Users']:
                    self.pool += 1
                    del self.game_num[i]['Users'][self.game_num[i]['Users'].index(user)]
                    if len(game_num[i]['Users']) == 0:  #重置该桌的状态
                        self.game_num[i]['Users'] =[]
                        self.game_num[i]['Process']=None
                        # {'Users':[],'Process':None,'UserExit':self.sendUserOutMsg}
                    break
    #用户登陆
    def login(self,userInfo):
        if userInfo.checkAuth(self.game_num) and self.pool != 0:  # 认证用户 #检测玩家是否满员
            userInfo.sendMessage(userInfo.convert('login','ok'))
        else:
            userInfo.sendMessage(userInfo.convert('login','error'))
            return 
        for i in self.game_num: #安排座位
            if len(self.game_num[i]['Users']) < 3:
                self.pool-=1
                self.game_num[i]['Users'].append(userInfo)
                print('玩家来自',userInfo.addr,'登录',end='\n请输入要执行的命令>')
                if len(self.game_num[i]['Users']) == 3 and self.game_num[i]['Process']==None:
                    p = multiprocessing.Process(target=self.start_game, args=(self.game_num[i], i))  # 创建新的进程来管理这桌游戏
                    p.start()
                    self.game_num[i]['Process'] = p
                else:
                    self.game_num[i]['Communication'][1].send(userInfo) #当人数不满３人时，已经有新的进程的时候，使新人加入该桌游戏
                break



    #开始这桌的游戏
    @staticmethod
    def start_game(d_msg,num):
        t = Thread(target=chat,args=(d_msg['Users'],))
        t.start()
        # 将发牌导出到列表
        paly1, paly2, paly3, dipai = fapai()
        paly1_fh = paixu(paly1)
        paly2_fh = paixu(paly2)
        paly3_fh = paixu(paly3)
        dipai_fh = paixu(dipai)
        d_msg['Users'][0].sendMessage(d_msg['Users'][0].convert(repr(paly1_fh),'puker'))
        d_msg['Users'][1].sendMessage(d_msg['Users'][1].convert(repr(paly2_fh),'puker'))
        d_msg['Users'][2].sendMessage(d_msg['Users'][2].convert(repr(paly3_fh),'puker'))

        for i in d_msg['Users']:
            msg = i.convert('开始游戏','msg')
            i.sendMessage(msg)
        t.join()

    #GM命令
    def gameCommand(self):
        while True:
            command=input('请输入要执行的命令>')
            try:
                if command=='game_list':
                    print(self.game_num)
                else:
                    eval(command)
            except Exception:
                print('没有此命令')