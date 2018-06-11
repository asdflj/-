import pygame
from settings import Settings
import sys
from gamefunction import *
import math

class Main:
    def __init__(self,user):
        self.user = user  #用户类
        self.Set = Settings() #加载设置
        self.poker = self.loadPackge()  # 加载扑克牌 资源包
        self.screen = pygame.display.set_mode((self.Set.screenWidth,self.Set.screenHeight))  #设置窗口
        pygame.display.set_caption('斗地主') #设置标题
        pygame.event.set_blocked(pygame.MOUSEMOTION | pygame.MOUSEBUTTONDOWN | pygame.QUIT) #设置监听事件 测试用
        self.drawBackGroundImage() #设置背景

    def drawBackGroundImage(self):
        '''绘制背景图片'''
        self.backgroundImg =  pygame.image.load(self.Set.backgroundImage)
        self.screen.blit(self.backgroundImg, (0, -24))  # 绘制背景图片
        self.Myself = self.drawSelf()  # 绘制自己
        self.leftUser = self.drawLeftUser() #绘制左边玩家
        self.rightUser = self.drawRightUser() #绘制右边玩家
        self.drawOutPokerArea(self.poker[:20]) #绘制出牌区域
        self.mouse = Mouse(self.screen) #鼠标点击点绘制 用来判断精灵是否碰撞
        self.Myself.showCard(self.poker[:10]) #绘制手牌

    def gameEvent(self):
        '''处理事件
           请使用装饰器进行重写
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse.drawPoint()
                print(self.Myself.pokers)
                print(self.mouse.rect)
                rect = pygame.sprite.spritecollideany(self.mouse,self.Myself.pokers)
                for i in self.Myself.pokers.sprites():
                    if rect == i.rect:
                        print(i.ID)
                        if i.pop == False:
                            i.pop = True
                        else:
                            i.pop = False
                        print('图像',i.rect)

    def main_loop(self):
        '''流程主循环
           请使用装饰器进行重写
        '''
        while True: #主事件循环
            self.drawBackGroundImage() #测试背景覆盖
            self.gameEvent()  #处理事件
            self.Myself.blitme() #绘制自己
            self.leftUser.blitme() #绘制左边玩家
            self.rightUser.blitme() #绘制右边玩家
            pygame.display.flip()

    def drawSelf(self): #初始化绘制自己
        '''绘制自己'''
        return PSelf(pygame,self.Set.nongmin,self.screen)

    def drawRightUser(self):
        '''绘制右边玩家'''
        return PRight(pygame, self.Set.otherNongmin, self.screen)

    def drawLeftUser(self):
        '''绘制左边玩家'''
        return PLeft(pygame, self.Set.otherDizhu, self.screen)

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
                rect = self.screen.blit(i.image,(120+x,200)) #绘制到屏幕上

    def loadPackge(self):
        '''加载扑克资源包'''
        print('加载资源包完成')
        return self.Set.poker