import re
from time import ctime
import os

''' 简单TCP通讯协议
    author ： 854865755
    Create on Sat May 26 12:27:42 2018
	statu  :  Finish
'''


class My_ptl:
    def __init__(self, sockfd, BUFFERSIZE=1024):
        '''初始化该协议
        sockfd(套接字),BUFFERSIZE(缓冲区大小)默认为1024'''
        self.__sockfd = sockfd
        self.addr = sockfd.getpeername()
        self.host, self.port = self.addr
        self.fileno = self.__sockfd.fileno()
        self.BUFFERSIZE = BUFFERSIZE

    def baseUserPwd(self, username, password, title):
        '''提供基础的用户名密码转换为标准协议格式'''
        return self.convert('username:%s,password:%s' % (username, password), title)

    def getSockfd(self):
        '''返回套接字'''
        return self.__sockfd

    def convert(self, data, title, data_type='str'):
        '''把数据转换为标准协议
           dataType str or file
        '''
        titleLength = len(title)+9
        ctimeLength = 38
        headSize = 13+titleLength+ctimeLength
        if data_type == 'str':
            if len(data) < 1000000000:
                ldata = len(data.encode())+2+headSize
                ldata = str(ldata).ljust(10, 'x')
                result = "{'length': %(ldata)s, 'title': '%(title)s', 'time': '%(time)s', 'data': '%(data)s'}" %\
                    {'ldata': ldata, 'title': title, 'data': data, 'time': ctime()}
            else:
                raise '文本长度太长'
        elif data_type == 'file':
            fileName = data
            if not os.path.isfile(fileName):
                raise '文件不存在'
            fileSize = os.path.getsize(fileName)
            if not fileSize:
                raise '文件长度为0'
            with open(fileName, 'rb')as fp:
                fileData = repr(fp.read())
                result = "{'length': %(fileSize)s, 'title': '%(title)s', 'time': '%(time)s', 'data': %(data)s}" %\
                    {'fileSize': str(len(fileData)+headSize).ljust(10, 'x'),
                     'title': title, 'time': ctime(), 'data': fileData}
        else:
            raise '类型错误'
        return PData(result, self.BUFFERSIZE)

    def splitUserPwd(self, data):
        '''提供基础的分割字符中的用户名和密码返回为元组
        第一个是用户名，第二个是密码'''
        username = data.split(',')[0].split(':')[1]
        password = data.split(',')[1].split(':')[1]
        return (username, password)

    def recv(self,callback=None):
        '''按照标准协议接收并返回一个可迭代对象'''
        bdata = bytes()
        data = self.__sockfd.recv(21)
        length = self.__get_recv_length(data.decode())
        bdata += b"{'length': %d" % length
        while True:
            if length > self.BUFFERSIZE:
                data = self.__sockfd.recv(self.BUFFERSIZE)
            else:
                data = self.__sockfd.recv(length)
            length -= self.BUFFERSIZE
            bdata += data
            if callback != None:  #每次接收回调函数，默认为空可用于获取速度
                callback()
            if length <= 0:
                return PData(bdata, self.BUFFERSIZE)

    @staticmethod
    def __get_recv_length(data):
        '''获取文本中的数字'''
        length = re.search('(\d+)', data).group()
        if length:
            return int(length)
        return 0

    def getMessage(self, convertToDict=False):
        '''接收信息
        convertToDict 是否转换为字典格式'''
        data = self.recv()
        if convertToDict:
            return eval(data.getAll())
        else:
            return data.getAll()

    def sendMessage(self, object):
        '''发送信息object为生成的协议对象'''
        for i in object:
            self.__sockfd.send(i.encode())
        return True

    def closeSockfd(self):
        '''关闭套接字'''
        self.__sockfd.close()


class PData:
    '''使其方便使用接收到的数据 不需要在意'''
    def __init__(self, data, BUFFERSIZE=1024):
        self.__data = data
        self.BUFFERSIZE = BUFFERSIZE

    def __iter__(self):
        self.__cur_pos = 0
        return self

    def __next__(self):
        while True:
            self.__cur_pos += 1
            result = self.__data[self.BUFFERSIZE *(self.__cur_pos - 1):self.BUFFERSIZE * self.__cur_pos]
            if not len(result):
                raise StopIteration
            return result

    def getAll(self):
        return self.__data

    def setBufferSize(self, size):
        '''设置输出的信息长度'''
        self.BUFFERSIZE = size
    def __str__(self):
        return self.__data

    def __repr__(self):
        return 'PData(%s, %s)'%(self.__data, self.BUFFERSIZE)
