from select import *
import time
from threading import Thread
from test import *

#初始化服务类
class Game:
    def __init__(self,roomInfo,roomNumber):
        self.roomInfo = roomInfo
        self.roomNumber = roomNumber
        self.users =  roomInfo['Users']
        self.pid = roomInfo['Process']
        self.userJoin = roomInfo['Communication'][0]
        self.userOut = roomInfo['UserExit']
        t = Thread(target=self.waitUserJoin)   #循环等待用户接入
        t.setDaemon(True)
        t.start()
        # t1 = Thread(target=self.getMessage)  #启用消息处理
        # t1.setDaemon(True)
        # t1.start()  #改为游戏主流程来控制消息接收

    #接收消息并发给处理函数
    def getMessage(self):
        #初始化监听列表
        rlist = []
        wlist = []
        xlist = []
        for user in self.users:
            rlist.append(user.getSockfd())
        while True:
            #如果没有满人就尝试加入新的监听套接字
            if len(rlist) !=3:
                rlist = []
                for user in self.users:
                    rlist.append(user.getSockfd())
            try:
                rs, ws, xs = select(rlist, wlist, xlist)
                user = self.getUser(rs)  #获取接收到的套接字属于哪个用户
                msg = eval(user.getMessage().decode())  #接收并处理消息
                self.handler(user,msg,rlist) #处理消息
            except (BrokenPipeError,AttributeError): #玩家退出 套接字连接失效
                self.playerExit(user,rlist)  #处理玩家退出信息
        time.sleep(0.1)

    def playerExit(self,user,rlist):
        getUserIndex = self.users.index(user)
        self.userOut.send(user.fileno)  #发送给主进程用户信息使其删除该用户
        del self.users[getUserIndex]
        del rlist[rlist.index(user.getSockfd())]  #清理信息
        self.sendRoomMessage(str(getUserIndex),'PlayOut' )  #告知其他玩家该用户已退出

    #等待用户加入
    def waitUserJoin(self):
        while True:
            user = self.userJoin.recv()
            self.users.append(user)

    #获取接收到的套接字属于哪个用户
    def getUser(self,rlist):
        for user in self.users:
            for i in rlist:
                if user.getSockfd() is i:
                    return user

    #处理接收到的信息
    def handler(self,user,msg,rlist):
        if msg['title'] == 'msg':
            self.sendRoomMessage(msg['data'],'msg',user)
        elif msg['title'] == 'loginOut':
            self.playerExit(user, rlist)
            user.closeSockfd()

    #发送消息给其他人
    def sendRoomMessage(self,msg,title,user=None):
        for i in self.users:
            if i is not user:
                send_msg = i.convert(msg,title)  # 把消息转换成协议格式
                i.sendMessage(send_msg)

    def startGame(self):
            self.sendRoomMessage('开始', 'msg')
            # while 1:
            #     pass
            # 执行游戏流程
            # 将发牌导出到列表
            # paly1, paly2, paly3, dipai = fapai()
            # paly1_fh = paixu(paly1)
            # paly2_fh = paixu(paly2)
            # paly3_fh = paixu(paly3)
            # dipai_fh = paixu(dipai)
            # self.users[0].sendMessage(self.users[0].convert(repr(paly1_fh), 'puker'))
            # self.users[1].sendMessage(self.users[1].convert(repr(paly2_fh), 'puker'))
            # self.users[2].sendMessage(self.users[2].convert(repr(paly3_fh), 'puker'))
            self.process()   #流程循环迭代

    def process(self):  #方案1使用迭代的方式来执行游戏的进程
        pass
    # if not user.puker:
    #     return