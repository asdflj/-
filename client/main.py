from login_window import Screen
from gamemain import Main
from socket import *

def main():
    sockfd = socket()
    sockfd.connect(('127.0.0.1',8888))
    mainWindow = Screen(sockfd)
    if mainWindow.closeStuta:
        gameWindow = Main(mainWindow.user)
        # gameWindow = Main('')
        gameWindow.main_loop()


if __name__ == '__main__':
    main()