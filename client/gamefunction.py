import pygame
import math

class Player:
    def __init__(self,pygame,packge,screen):
        self.pygame = pygame
        self.packge = packge #资源包
        self.image = self.packge.otherNongmin  #设置角色图片
        self.screen = screen
        self.rect = self.image.get_rect()
        self.cardBackGround = self.packge.cardBackGround #提示剩余牌图片
        self.font = self.packge.font #字体

    def blit(self):
        self.screen.blit(self.image,self.rect)   #绘制角色图片

    def showCard(self,poker):
        '''绘制剩余牌数在角色旁边 poker = 角色剩余的牌 以数组的形式'''
        self.screen.blit(self.cardBackGround,(self.cardX,self.cardY))
        length = len(poker)
        text = self.font.render('%s'%length, True, (0,0,0))  #显示剩余多少张牌
        self.screen.blit(text,(self.cardX+50,self.cardY+20)) #绘制到屏幕上

    def selectDiZhu(self):
        '''选择地主'''
        self.screen.blit(self.packge.points[1].image,(self.pointX,self.pointY))

    def changeImage(self,image):
        self.image = image  #改变角色图片

    def pushCard(self):
        pass


class PSelf(Player):
    def __init__(self,pygame,packge,screen):
        super(PSelf,self).__init__(pygame,packge,screen)
        self.rect.x = 50     #设置角色位置
        self.rect.y = 450
        self.pokers = pygame.sprite.Group()  # 要绘制的手牌  精灵组类型
        self.pointGroup = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.cardX = 30   #提示牌位置
        self.cardY = 400
        self.pointX = 300  #叫分图片位置
        self.pointY = 360

    def pushCard(self):
        '''绘制出牌按钮 过按钮'''
        self.buttons.empty()
        rect = self.screen.blit(self.packge.put.image,(self.packge.put.x,self.packge.put.y))
        self.packge.put.setRect(rect)
        self.buttons.add(self.packge.put)
        rect = self.screen.blit(self.packge.pass1.image,(self.packge.pass1.x,self.packge.pass1.y))
        self.packge.pass1.setRect(rect)
        self.buttons.add(self.packge.pass1)

    def showCard(self,poker):
        '''绘制手上的手牌 poker=列表 (里面放入扑克牌对象)'''
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
                rect = self.screen.blit(i.image, (120 + x, 430-20))  # 绘制到屏幕上
            i.setRect(rect)
            self.pokers.add(i)  #添加到组

    def selectDiZhu(self):
        '''选地主'''
        self.pointGroup.empty()
        x= self.pointX
        for point in self.packge.points:
            rect = self.screen.blit(point.image,(x,self.pointY)) #绘制叫分图片
            point.setRect(rect)
            self.pointGroup.add(point)
            x+=100


    def getPointGroup(self):
        '''获取叫分图片组'''
        return self.pointGroup

    def getButtonGroup(self):
        '''获取出牌 过 图片组'''
        return self.buttons

    def getPokerGroup(self):
        '''获取扑克组'''
        return self.pokers

class PLeft(Player):
    def __init__(self,pygame,packge,screen):
        super(PLeft,self).__init__(pygame,packge,screen)
        self.image = self.pygame.transform.rotate(self.image,-130)
        self.rect.x = 0     #设置位置
        self.rect.y = -15
        self.cardX = 200
        self.cardY = 40
        self.pointX = 700
        self.pointY = 100

class PRight(Player):
    def __init__(self,pygame,packge,screen):
        super(PRight,self).__init__(pygame,packge,screen)
        self.image = self.pygame.transform.rotate(self.image,130)
        self.rect.x = 810     #设置位置
        self.rect.y = -15
        self.cardX = 750
        self.cardY = 40
        self.pointX = 200
        self.pointY = 100

class Poker(pygame.sprite.Sprite):
    def __init__(self,path,ID):
        super(Poker, self).__init__()
        self.path = path
        self.ID = ID
        self.image = pygame.image.load(path)
        self.pop = False
        # self.image =pygame.transform.scale(self.image, (40, 50))

    def setRect(self,rect):
        self.rect =rect

class Mouse(pygame.sprite.Sprite):
    '''鼠标类 在鼠标点击的一个地方动态创建一个精灵用于检测图片碰撞'''
    def __init__(self,screen):
        super(Mouse, self).__init__()
        self.screen = screen
        self.width = 1
        self.height = 1

    def getPos(self):
        return pygame.mouse.get_pos()

    def drawPoint(self):
        '''在指定的一个位置绘制图片'''
        mouse_x,mouse_y =self.getPos()
        self.rect = pygame.Rect(mouse_x,mouse_y,self.width,self.height)
        pygame.draw.rect(self.screen,(255,255,255),self.rect)

class Point(pygame.sprite.Sprite):
    '''以精灵的方式创建叫分图片'''
    def __init__(self,path,point):
        super(Point, self).__init__()
        self.path = path
        self.image = pygame.image.load(self.path)
        self.point = point

    def setRect(self,rect):
        self.rect = rect

class Buttons(pygame.sprite.Sprite):
    '''以精灵的方式创建出牌 过图片'''
    def __init__(self,path,x,y,put):
        super(Buttons, self).__init__()
        self.path = path
        self.image = pygame.image.load(self.path)
        self.x = x
        self.y = y
        self.putCard = put

    def setRect(self,rect):
        self.rect = rect



