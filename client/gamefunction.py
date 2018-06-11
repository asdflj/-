import pygame
class Player:
    def __init__(self,pygame,image,screen):
        self.pygame = pygame
        self.image = self.pygame.image.load(image)
        self.screen = screen
        self.rect = self.image.get_rect()
    def blitme(self):
        self.screen.blit(self.image,self.rect)

class PSelf(Player):
    def __init__(self,pygame,image,screen):
        super(PSelf,self).__init__(pygame,image,screen)
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        self.rect.x = 50     #设置位置
        self.rect.y = 450
    def showCard(self,Poker):
        pass
        # for i in Puker:
            # image = self.pygame.image.load()


class PLeft(Player):
    def __init__(self,pygame,image,screen):
        super(PLeft,self).__init__(pygame,image,screen)
        self.image = self.pygame.transform.rotate(self.image,-130)
        self.rect.x = 0     #设置位置
        self.rect.y = -15


class PRight(Player):
    def __init__(self,pygame,image,screen):
        super(PRight,self).__init__(pygame,image,screen)
        self.image = self.pygame.transform.rotate(self.image,130)
        self.rect.x = 810     #设置位置
        self.rect.y = -15

class Poker(pygame.sprite.Sprite):
    def __init__(self,path,ID):
        super(Poker, self).__init__()
        self.path = path
        self.ID = ID
        self.image = pygame.image.load(path)
        # self.image =pygame.transform.scale(self.image, (40, 50))
        # self.rect = self.image.get_rect()

    def setRect(self,rect):
        self.rect =rect
    def up(self):
        self.rect.top +=50;

    def down(self):
        self.rect  -=50;
class Mouse(pygame.sprite.Sprite):
    def __init__(self,screen):
        super(Mouse, self).__init__()
        self.screen = screen
        self.width = 10
        self.height = 10
    def getPos(self):
        return pygame.mouse.get_pos()
    def drawPoint(self):
        mouse_x,mouse_y =self.getPos()
        self.rect = pygame.Rect(mouse_x,mouse_y,self.width,self.height)
        pygame.draw.rect(self.screen,(255,255,255),self.rect)
