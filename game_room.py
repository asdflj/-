from select import *
import time

#初始化服务类


class Game:
    def __init__(self,roomInfo,roomNumber):
        self.roomInfo = roomInfo
        self.roomNumber = roomNumber
        self.users =  roomInfo['Users']
        self.pid = roomInfo['Process'].pid
        self.userJoin = roomInfo['Communication'][0]
    #接收消息
    def getMessage(self):
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
                    rlist.append(user)
            rs, ws, xs = select(rlist, wlist, xlist)
            user = self.getUser(rs)
            try:
                msg = eval(user.getMessage().decode())
                self.handler(user,msg)
            except Exception as e:
                print(e)


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
            self.sendRoomMessage(user,msg['data'])
        elif msg['title'] == 'loginOut':
            user.closeSockfd()

    #发送消息给其他人
    def sendRoomMessage(self, user, msg):
        for i in self.users:
            if i is not user:
                send_msg = i.convert(msg, 'msg')  # 把消息转换成协议格式
                i.sendMessage(send_msg)


def chat(users):
    rlist = []
    for user in users:
        rlist.append(user.getSockfd())
    wlist = []
    xlist = []
    while True:
        #检测连接数是否满足3个
        if len(rlist) !=3:
            rlist = []
            for user in users:
                rlist.append(user.getSockfd())
        #设置监听套接字列表
        rs, ws, xs = select(rlist, wlist, xlist)
        for user in users:
            for i in rs:
                if user.getSockfd() is i:
                    try:
                        msg = eval(user.getMessage().decode())  #解析消息
                        if msg['title']=='msg':   #发送信息给其他人
                            sendRoomMessage(users,user,msg['data'])
                        elif msg['title']=='loginOut':
                            user.closeSockfd()
                            
                        break
                    except Exception as e:
                        print(e)
                        del users[users.index(user)]
                        del rlist[rlist.index(i)]
                        player_exit(users)
        time.sleep(0.1)

def sendRoomMessage(users,user,msg):
    for i in users:
        if i is not user:
            send_msg=i.convert(msg,'msg')  #把消息转换成协议格式
            i.sendMessage(send_msg)

def player_exit(users): #通告其他玩家此玩家已经退出
    # for user in users:
    #     user.protocal('play_exit')
    pass
def get