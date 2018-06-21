from socket import *
from protocol1 import My_ptl as Protocal
import sys
from threading import Thread
from random import  randrange
sockfd = socket(AF_INET, SOCK_STREAM, 0)
sockfd.connect(('127.0.0.1', 8888))

p=Protocal(sockfd)
sys.argv.append(randrange(1,100))
msg =p.baseUserPwd(sys.argv[1],'123456','login')

p.sendMessage(msg)

def recv_msg(sockfd):
    while True:
        data = sockfd.getMessage()
        print(data.decode())
t =Thread(target=recv_msg,args=(p,))
t.start()
while True:
    msg = input('发消息')
    # msg =p.base_user_pwd(sys.argv[1],'123456','login')
    # msg = p.convert(msg,'msg')
    # print(msg)
    msg = p.convert(msg,'msg')
    p.sendMessage(msg)
    # print(sockfd.recv(1024).decode())

p.closeSockfd()
