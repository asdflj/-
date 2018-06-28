import pymysql
from protocol1 import My_ptl as Protocal


class User(Protocal):
    '''用户类'''
    def __init__(self,sockfd):
        super(User, self).__init__(sockfd)

    def checkAuth(self,game_num):
        '''认证用户'''
        for i in game_num:
            for j in game_num[i]['Users']:
                if j.username == self.username:
                    return False
        if True:
            return True
        else:

            return False

    def register(self,data):
        '''注册用户'''
        username ,password = self.splitUserPwd(data)
        #执行注册操作
        if True:
            msg = self.convert("True",'register')
        else:
            msg = self.convert("False", 'register')
        self.sendMessage(msg)

    def setUserPwd(self,user):
        '''user格式(username,passsword)'''
        self.username,self.password=user
    def setpoker(self,poker):
        '''设置扑克'''
        self.poker=poker
    def setname(self,name):
        '''设置用户名'''
        self.name=name
    def setId(self,id):
        '''设置该用户是否是地主'''
        self.id = id
    def closeSockfd(self):
        '''用户登出'''
        self.sendMessage(self.convert('ok','loginOut'))
        super(User, self).closeSockfd()