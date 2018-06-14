import pygame
from settings import Settings
import sys
from gamefunction import *
import math

class Main:
    def __init__(self,user):
        pygame.init()
        self.user = user  #用户类
        self.Set = Settings() #加载设置
        self.screen = pygame.display.set_mode((self.Set.screenWidth,self.Set.screenHeight))  #设置窗口
        self.packge = self.loadPackge()  # 加载资源包
        pygame.display.set_caption('斗地主') #设置标题
        pygame.event.set_blocked(pygame.MOUSEMOTION | pygame.MOUSEBUTTONDOWN | pygame.QUIT) #设置监听事件 测试用
        #初始化要绘制的信息

        self.mySelf = self.drawSelf()  # 绘制自己
        self.leftUser = self.drawLeftUser() #绘制左边玩家
        self.rightUser = self.drawRightUser() #绘制右边玩家
        self.mouse = Mouse(self.screen) #鼠标点击点绘制 用来判断精灵是否碰撞

    def drawBackGroundImage(self):
        '''绘制背景图片'''
        self.screen.blit(self.packge.backgroundImg, (0, -24))  # 绘制背景图片

    def gameEvent(self):
        '''处理事件
           请使用装饰器进行重写
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse.drawPoint()
                rect = pygame.sprite.spritecollideany(self.mouse,self.mySelf.getPokerGroup())
                for i in self.mySelf.getPokerGroup().sprites():
                    if rect == i.rect:
                        print(i.ID)
                        if i.pop == False:
                            i.pop = True
                        else:
                            i.pop = False

                rect = pygame.sprite.spritecollideany(self.mouse, self.mySelf.getButtonGroup())
                for i in self.mySelf.getButtonGroup().sprites():
                    if rect == i.rect:
                        print('图像',i.putCard)


    def main_loop(self):
        '''流程主循环
           请使用装饰器进行重写
        '''
        while True: #主事件循环
            self.drawBackGroundImage() #背景覆盖
            self.drawOutPokerArea(self.packge.poker[:20])  # 绘制出牌区域
            self.mySelf.showCard(self.packge.poker[:10])  # 绘制手牌
            self.rightUser.showCard((self.packge.poker[1:])) # 绘制手牌
            self.leftUser.showCard((self.packge.poker[1:]))  # 绘制手牌
            self.mySelf.pushCard()
            # self.mySelf.selectDiZhu()
            # self.rightUser.selectDiZhu()
            # self.leftUser.selectDiZhu()
            self.gameEvent()  #处理事件
            self.mySelf.blit() #绘制自己
            self.leftUser.blit() #绘制左边玩家
            self.rightUser.blit() #绘制右边玩家
            pygame.display.flip()

    def drawSelf(self): #初始化绘制自己
        '''绘制自己'''
        player = PSelf(pygame, self.packge, self.screen)
        player.changeImage(self.packge.nongmin)
        return player

    def drawRightUser(self):
        '''绘制右边玩家'''
        return PRight(pygame, self.packge,self.screen)

    def drawLeftUser(self):
        '''绘制左边玩家'''
        return PLeft(pygame, self.packge,self.screen)

    def drawOutPokerArea(self,poker=None):
        '''绘制出牌区域'''
        #############计算绘制位置 ###############
        if poker:
            width = 700
            # height = 150
            # area = pygame.Surface((width,height))  #创建矩形
            # area.fill((0,0,255))  #填充矩形
            # area.set_colorkey((0,0,255)) #设置透明颜色
            if len(poker)*150>width:  #判断牌数量是否能存放下完整大小
                lenght = math.floor(width / (len(poker)+1))
            else:
                lenght = 105;
        #########################################
            x = 0
            #把要绘制的扑克牌绘制出来
            for i in poker:
                x +=lenght
                self.screen.blit(i.image,(120+x,200)) #绘制到屏幕上

    def loadPackge(self):
        '''加载扑克资源包'''
        class packge:
            def __init__(self,pygame,settings):
                self.pygame =pygame
                self.settings = settings
                self.poker = [Poker('%s\\%s.jpg' % (self.settings.poker, i), i) for i in range(1, 55)] #加载扑克牌
                self.backgroundImg = pygame.image.load(self.settings.backgroundImage)  # 设置背景
                self.font = pygame.font.SysFont(self.settings.font, 16)  # 加载字体
                self.cardBackGround = pygame.image.load(self.settings.cardBackGround)  # 加载卡牌背景
                point = [self.settings.point0,self.settings.point1,self.settings.point2,self.settings.point3]
                self.points = [Point(point[x],x) for x in range(4)] # 加载叫分图片
                self.pass1 = Buttons(self.settings.pass1,600,360,False)
                self.put = Buttons(self.settings.put,300,360,True)
                self.putError = pygame.image.load(self.settings.putError)
                self.putNoCards = pygame.image.load(self.settings.putNoCards)
                self.nongmin = pygame.image.load(self.settings.nongmin)
                self.otherDizhu = pygame.image.load(self.settings.otherDizhu)
                self.otherNongmin = pygame.image.load(self.settings.otherNongmin)
        print('加载资源包完成')
        return packge(pygame,self.Set)