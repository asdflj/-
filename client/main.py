from login_window import Screen
from gamemain import Main
from socket import *
from addr import *
def main():
    sockfd = socket()
    sockfd.connect(('192.168.237.130',8888))
    mainWindow = Screen(sockfd)
    if mainWindow.closeStuta:
        gameWindow = Main(mainWindow.user)
        # gameWindow = Main('')
        gameWindow.main_loop()


if __name__ == '__main__':
    main()