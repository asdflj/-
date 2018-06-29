import signal
import sys
import os
from new_server import Server
from createDatabase import MysqlCreate
def initServer():
    if len(sys.argv)<3:
        print('启用默认参数')
        sys.argv[1:2]='127.0.0.1','8888'
    HOST,PORT = sys.argv[1],int(sys.argv[2])
    return HOST,PORT

def main():
    '''初始化服务器'''
    if os.name!='nt':
        signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    # mysql = MysqlCreate() #初始化数据库
    # mysql.rgert()
    
    GAME_POOL=30*3
    HOST,PORT=initServer()
    SERVER = Server(HOST,PORT,GAME_POOL) #初始化该服务器
    SERVER.serve_forever()

if __name__ =='__main__':
    main()