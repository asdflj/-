import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QTextEdit,QGridLayout,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon
import PyQt5.QtCore

class login(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        with open('style.css') as fp:
            self.app.setStyleSheet(fp.read())
        super().__init__()
        self.initUI()
        sys.exit(self.app.exec_())

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('斗地主')
        self.createlayout()
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        self.show()
    def createlayout(self):

        # username = QLabel('用户名:',self)
        # password = QLabel('密码:',self)
        btnlogin = QPushButton('登陆',self)
        # btnregister = QPushButton('注册',self)
        # usernameEdit = QLineEdit('',self)
        # passwordEdit = QLineEdit('',self)
        # username.setObjectName('username')
        # password.setObjectName('password')
        btnlogin.setObjectName('btn-login')
        # btnlogin.set
        # btnregister.setObjectName('btn-register')
        # usernameEdit.setObjectName('username-edit')
        # passwordEdit.setObjectName('passwrold-edit')
        # grid = QGridLayout()
        # grid.setSpacing(10)
        # grid.addWidget(username, 1, 0)
        # grid.addWidget(usernameEdit,1,1)
        # grid.addWidget(password, 2, 0)
        # grid.addWidget(passwordEdit,2,1)
        # grid.addWidget(btnlogin,5,1)
        # grid.addWidget(btnregister, 5, 0)
        # self.setLayout(grid)





