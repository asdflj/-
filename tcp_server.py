from socket import *
from protocol1 import My_ptl as Protocal
sockfd = socket(AF_INET, SOCK_STREAM, 0)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('127.0.0.1', 8888))

sockfd.listen(15)
while True:
    # try:
    print('waiting for connect')
    connfd, address = sockfd.accept()
    print('connect from', address)
#     print(connfd.recv(21))
    p=Protocal(connfd)
    data=eval(p.getMessage().decode())
    print(data)
    # with open('sdaf.txt','wb')as file:
    #     file.write(data['data'])
    # except Exception as e:
    #     print(e)
    #     continue
    # size=os.path.getsize('tcp_client.py')
    # # with open('tcp_client.py','rb')as file:
    # #     s='{"size":%s,"data":%s}'%(size,file.read())
    #     connfd.send(s.encode())
    # with open('tcp_client.py', 'rb')as file:
    #     while True:
    #         data = file.read(15)
    #         if not data:
    #             break
    #         connfd.send(data)

    # connfd.close()

sockfd.close()
