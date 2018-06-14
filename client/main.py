from login_window import Screen
from gamemain import Main

def main():

    mainWindow = Screen()
    gameWindow = Main('')
    gameWindow.main_loop()



if __name__ == '__main__':
    main()