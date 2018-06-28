import pymysql
from protocol1 import My_ptl as Protocal


class User(Protocal):
    '''用户类'''
    def __init__(self,sockfd):
        super(User, self).__init__(sockfd)
        self.id = 0

    def checkAuth(self,game_num):
        '''认证用户'''
        for i in game_num:
            for j in game_num[i]['Users']:
                if j.username == self.username:
                    return False
        return True

    def register(self):
        '''注册用户'''
        pass
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