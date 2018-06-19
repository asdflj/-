from protocol1 import My_ptl as Protocal


class User(Protocal):
    def login(self,MessageBox,username,password):
        '''登陆操作'''
        if True:
            MessageBox('登陆', '登陆成功!')
            self.username = username
            self.password = password
            return True
        else:
            MessageBox('登陆', '登陆失败!')
            return False
    def register(self,MessageBox,username,password):
        '''注册操作'''
        if True:
            MessageBox('注册', '注册成功!')
            return True
        else:
            MessageBox('注册', '注册失败!')
            return False
