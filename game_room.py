from select import *
import time

def chat(users):
    rlist = []
    for user in users:
        rlist.append(user.getSockfd())
    wlist = []
    xlist = []
    while True:
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