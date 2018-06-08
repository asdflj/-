# import pygame
# import time
# from settings import Settings as Set
from login_window import login

def main():
    window = login()
    # app = QtWidgets.QApplication(sys.argv)
    # window = QtWidgets.QWidget()
    # window.resize(480,320)
    # window.setWindowTitle('斗地主')
    # label1 = QLabel('test',app)
    # window.show()
    # exit(app.exec_())
    # b = pygame.image.load(Set.backgroundImage)
    # screen = pygame.display.set_mode((1000,624))
    # pygame.display.set_caption('斗地主')
    # while  True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #     screen.blit(b,(0,0))
    #     pygame.display.flip()
    #     # time.sleep(0.1)

if __name__ == '__main__':
    main()