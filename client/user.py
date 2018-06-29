from protocol1 import My_ptl as Protocal


class User(Protocal):
    def login(self,MessageBox,username,password):
        '''登陆操作'''
        msg = self.baseUserPwd(username,password,'login')
        self.sendMessage(msg)
        msg = self.getMessage(True)
        print(msg)
        if msg['title'] == 'ok' :
            MessageBox('登陆', '登陆成功!')
            self.username = username
            self.password = password
            return True
        else:
            MessageBox('登陆', '登陆失败!')
            return False

    def register(self,MessageBox,username,password):
        '''注册操作'''
        msg = self.baseUserPwd(username,password,'register')
        self.sendMessage(msg)
        msg = self.getMessage(True)
        if msg['data'] == 'True' :
            MessageBox('注册', '注册成功!')
            return True
        else:
            MessageBox('注册', '注册失败!')
            return False

    def setPoker(self,poker):
        self.poker=poker

    def getPoker(self):
        return self.poker
    def closeSockfd(self):
        msg =self.convert('退出游戏','exit')
        self.sendMessage(msg)
        super(User, self).closeSockfd()