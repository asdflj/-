from select import *
import time
from threading import Thread
#初始化服务类
class Game:
    def __init__(self,roomInfo,roomNumber):
        self.roomInfo = roomInfo
        self.roomNumber = roomNumber
        self.users =  roomInfo['Users']
        self.pid = roomInfo['Process'].pid
        self.userJoin = roomInfo['Communication'][0]
        self.userOut = roomInfo['UserExit']
        t = Thread(target=self.waitUserJoin)   #循环等待用户接入
        t.setDaemon(True)
        t.start()
        t1 = Thread(target=self.getMessage)  #启用消息处理
        t1.setDaemon(True)
        t1.start()

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
            rs, ws, xs = select(rlist, wlist, xlist)
            user = self.getUser(rs)  #获取接收到的套接字属于哪个用户
            try:
                msg = eval(user.getMessage().decode())  #接收并处理消息
                self.handler(user,msg) #处理消息
            except BrokenPipeError: #玩家退出 套接字连接失效
                self.playerExit(rlist,user)  #处理玩家退出信息
        time.sleep(0.1)

    def playerExit(self,rlist,user):
        getUserIndex = self.users.index(user)
        self.userOut.send(user)  #发送给主进程用户信息使其删除该用户
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
    def handler(self,user,msg):
        if msg['title'] == 'msg':
            self.sendRoomMessage(msg['data'],'msg',user)
        elif msg['title'] == 'loginOut':
            user.closeSockfd()

    #发送消息给其他人
    def sendRoomMessage(self,msg,title,user=None):
        for i in self.users:
            if i is not user:
                send_msg = i.convert(msg,title)  # 把消息转换成协议格式
                i.sendMessage(send_msg)
