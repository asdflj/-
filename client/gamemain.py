import pygame
from settings import Settings
import sys
from gamefunction import *


class Main:
    def __init__(self,user):
        self.user = user
        self.Set = Settings() #加载设置
        self.screen = pygame.display.set_mode((1000, 600))  #设置窗口
        pygame.display.set_caption('斗地主')
        self.poker = self.loadPackge() #加载扑克牌
        self.drawBackGroundImage() #设置背景
        while True: #主事件循环
            self.handlerEvent()  #处理事件
            self.Myself.blitme() #绘制自己
            self.leftUser.blitme() #绘制左边玩家
            self.rightUser.blitme() #绘制右边玩家
            pygame.display.flip()

    def drawBackGroundImage(self):
        '''绘制背景图片'''
        self.backgroundImg =  pygame.image.load(self.Set.backgroundImage)
        self.screen.blit(self.backgroundImg, (0, -24))  # 绘制背景图片
        self.Myself = self.drawSelf()  # 绘制自己
        self.leftUser = self.drawLeftUser() #绘制左边玩家
        self.rightUser = self.drawRightUser() #绘制右边玩家

    def handlerEvent(self):
        '''处理事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def drawSelf(self): #初始化绘制自己
        '''绘制自己'''
        return PSelf(pygame,self.Set.nongmin,self.screen)

    def drawRightUser(self):
        '''绘制右边玩家'''
        return PRight(pygame, self.Set.otherNongmin, self.screen)

    def drawLeftUser(self):
        '''绘制左边玩家'''
        return PLeft(pygame, self.Set.otherDizhu, self.screen)

    def drawOutPokerArea(self):
        '''绘制出牌区域'''
        pass

    def loadPackge(self):
        '''加载扑克资源包'''
        poker = []
        for i in self.Set.poker:
            image = pygame.image.load(i).get_rect()
            poker.append(image)
        print('加载资源包完成')
        return poker