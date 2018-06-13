import pygame
import math

class Player:
    def __init__(self,pygame,image,screen,cardbg,font,score):
        self.pygame = pygame
        self.image = self.pygame.image.load(image)
        self.screen = screen
        self.rect = self.image.get_rect()
        # self.cardBackGround = self.pygame.image.load()
        self.cardBackGround = pygame.transform.scale(cardbg, (40, 50))  #缩放提示牌大小
        self.font = font
        self.score = score

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def showCard(self,poker):
        '''绘制剩余牌数在角色旁边'''
        self.screen.blit(self.cardBackGround,(self.cardX,self.cardY))
        length = len(poker)
        text = self.font.render('%s'%length, True, (0,0,0))
        self.screen.blit(text,(self.cardX+50,self.cardY+20))

    def selectDiZhu(self):
        '''选择地主'''
        pass
        # self.screen.blit(self.score,(self.scoreX,self.scoreY))

class PSelf(Player):
    def __init__(self,pygame,image,screen,cardbg,font,score):
        super(PSelf,self).__init__(pygame,image,screen,cardbg,font,score)
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        self.rect.x = 50     #设置位置
        self.rect.y = 450
        self.pokers = pygame.sprite.Group()  # 要绘制的手牌  精灵组类型
        self.cardX = 30
        self.cardY = 400
        self.scoreX = 500
        self.scoreY = 380

    def showCard(self,poker):
        '''绘制手上的手牌'''
        super(PSelf, self).showCard(poker)
        width = 700
        if len(poker) * 150 > width:  # 判断牌数量是否能存放下完整大小
            lenght = math.floor(width / (len(poker) + 1))
        else:
            lenght = 105;
        x = 0
        self.pokers.empty() #清空精灵组
        for i in poker:
            x += lenght
            if not i.pop:
                rect = self.screen.blit(i.image, (120  + x, 430)) #绘制到屏幕上
            else:
                rect = self.screen.blit(i.image, (120 + x, 430-50))  # 绘制到屏幕上
            i.setRect(rect)
            self.pokers.add(i)  #添加到组

    def selectDiZhu(self):
        super(PSelf, self).selectDiZhu()
        for score in self.score:

            pass

class PLeft(Player):
    def __init__(self,pygame,image,screen,cardbg,font,score):
        super(PLeft,self).__init__(pygame,image,screen,cardbg,font,score)
        self.image = self.pygame.transform.rotate(self.image,-130)
        self.rect.x = 0     #设置位置
        self.rect.y = -15
        self.cardX = 200
        self.cardY = 40

class PRight(Player):
    def __init__(self,pygame,image,screen,cardbg,font,score):
        super(PRight,self).__init__(pygame,image,screen,cardbg,font,score)
        self.image = self.pygame.transform.rotate(self.image,130)
        self.rect.x = 810     #设置位置
        self.rect.y = -15
        self.cardX = 750
        self.cardY = 40

class Poker(pygame.sprite.Sprite):
    def __init__(self,path,ID):
        super(Poker, self).__init__()
        self.path = path
        self.ID = ID
        self.image = pygame.image.load(path)
        self.pop = False
        # self.image =pygame.transform.scale(self.image, (40, 50))
        # self.rect = self.image.get_rect()

    def setRect(self,rect):
        self.rect =rect

class Mouse(pygame.sprite.Sprite):
    def __init__(self,screen):
        super(Mouse, self).__init__()
        self.screen = screen
        self.width = 1
        self.height = 1
    def getPos(self):
        return pygame.mouse.get_pos()
    def drawPoint(self):
        mouse_x,mouse_y =self.getPos()
        self.rect = pygame.Rect(mouse_x,mouse_y,self.width,self.height)
        pygame.draw.rect(self.screen,(255,255,255),self.rect)
