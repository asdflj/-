from protocol1 import My_ptl as Protocal


class User(Protocal):
    def login(self,MessageBox,username,password):
        '''登陆操作'''
        if self.baseUserPwd(username,password,'login'):
            MessageBox('登陆', '登陆成功!')
            self.username = username
            self.password = password
            return True
        else:
            MessageBox('登陆', '登陆失败!')
            return False

    def register(self,MessageBox,username,password):
        '''注册操作'''
        if self.baseUserPwd(username,password,'register'):
            MessageBox('注册', '注册成功!')
            return True
        else:
            MessageBox('注册', '注册失败!')
            return False

    def setPoker(self,poker):
        self.poker=poker

    def getPoker(self):
        return self.poker