import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QTextEdit,QLineEdit,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon,QBrush,QPixmap,QPalette,QRegExpValidator
from PyQt5.QtCore import Qt,QRegExp
from user import User

class Screen(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.initUI()
        self.user = User()
        self.app.exec_()

    def initUI(self):
        '''初始化UI界面'''
        self.setBackground()  #设置背景图片
        with open('css/style.css') as fp:   #读取并设置样式
            self.app.setStyleSheet(fp.read())
        self.setObjectName('main')     #设置样式ID为main
        self.setGeometry(300,300,800,480)  #设置窗体
        self.setWindowTitle('斗地主')
        self.setFixedHeight(480)
        self.setFixedWidth(800)
        self.createlayout()   #创建控件
        self.show()

    def setBackground(self):
        '''设置背景图片'''
        palette1 =QPalette()
        palette1.setBrush(self.backgroundRole(),QBrush(QPixmap(r'images/timg.jpg')))  #设置背景图片
        self.setPalette(palette1) #应用

    def createlayout(self):
        '''创建布局'''
        self.usernameEdit=self.createEdit('',(330,193),'normal','username-edit','[a-zA-Z0-9!@]+')  #用户名输入框
        self.passwordEdit=self.createEdit('',(330,250),'password','passwrold-edit','[a-zA-Z0-9!@]+') #密码输入框
        self.btnlogin = self.createButton('',(410,373),False,'btn-login',self.btnLoginClick,'hand') #登陆按钮
        self.btnregister = self.createButton('',(182,373),False,'btn-register',self.btnRegisterClick,'hand')#注册按钮

    def createEdit(self,text='',move=(0,0),model=None,id=None,validator=None): #创建文本框控件
        '''text =控件内容 Validator = 正则输入限制 id = 样式ID  move = 移动到(x,y)model = password or normal '''
        edit = QLineEdit(text, self)
        edit.move(*move)
        if model == 'password': #文本框显示模式
            edit.setEchoMode(QLineEdit.Password)
        else:
            edit.setEchoMode(QLineEdit.Normal)
        if validator:          #setvalidator 输入限制  QRegExp正则
            edit.setValidator(QRegExpValidator(QRegExp(validator), self))
        if id: #设置样式应用ID
            edit.setObjectName(id)
        return edit

    def createButton(self,text='',move=(0,0),display=True,id=None, clicked=None,cursor=None):
        '''text = 控件的内容 move = 移动到(x,y) display = 是否显示 id = 样式ID
        chilcked =点击后要执行的函数 cursor=鼠标'''
        button = QPushButton(text,self)
        button.setFlat(not display)  #是否显示
        button.move(*move)
        if id: #设置样式应用ID
            button.setObjectName(id)
        if cursor == 'hand': #鼠标形状
            button.setCursor(Qt.PointingHandCursor)
        elif cursor == None:
            pass
        else:
            button.setCursor(cursor)
        if type(clicked)== type(self.createButton): #点击时执行的函数
            button.clicked.connect(clicked)
        return button

    def btnLoginClick(self):
        '''点击了登陆按钮'''
        username, password = self.userInputCheck()
        if username == None or password == None: #判断
            self.myMessageBox('提示','用户名或密码不能为空')
            return
        if self.user.login(self.myMessageBox,username,password):
            self.close()

    def userInputCheck(self):
        '''检查用户名和密码长度 如果不够长返回false 够长返回 username 和 password'''
        username = self.usernameEdit.text() #获取文本框内容
        password = self.passwordEdit.text()
        if len(username) and len(password): #判断长度
            return (username, password)
        else:
            return (None, None)

    def myMessageBox(self,title,text):
        '''这个窗体的消息框'''
        QMessageBox.question(self, title,text, QMessageBox.Yes)

    def btnRegisterClick(self):
        '''点击了注册按钮'''
        username, password = self.userInputCheck()
        if username == None or password == None: #判断
            self.myMessageBox('提示','用户名或密码不能为空')
            return
        if self.user.register(self.myMessageBox,username,password):
            self.btnLoginClick()




