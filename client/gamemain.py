import pygame
from settings import Settings
import sys
from gamefunction import *
import math
from threading import Thread
import time

class Main:
    def __init__(self,user):
        pygame.init()
        self.user = user  #用户类
        self.Set = Settings() #加载设置
        self.screen = pygame.display.set_mode((self.Set.screenWidth,self.Set.screenHeight))  #设置窗口
        self.packge = self.loadPackge()  # 加载资源包
        pygame.display.set_caption('斗地主') #设置标题
        pygame.event.set_blocked(pygame.MOUSEMOTION | pygame.MOUSEBUTTONDOWN | pygame.QUIT) #设置监听事件 测试用
        self.events = {'touch':[],'display':[]} #要监听的事件
        #初始化要绘制的信息

        self.mySelf = self.drawSelf()  # 绘制自己
        self.leftUser = self.drawLeftUser() #绘制左边玩家
        self.rightUser = self.drawRightUser() #绘制右边玩家
        self.mouse = Mouse(self.screen) #鼠标点击点绘制 用来判断精灵是否碰撞

        self.t =Thread(target=self.getMessage)
        self.t.setDaemon(True)
        self.t.start()

    def drawBackGroundImage(self):
        '''绘制背景图片'''
        self.screen.blit(self.packge.backgroundImg, (0, -24))  # 绘制背景图片

    def getMessage(self):
        while True:
            # msg = self.user.getMessage(True)
            time.sleep(1)
            msg={'data':'选地主','title':'选地主'}
            if msg['title'] =='选地主':
                self.appendDisplayEvents(self.mySelf.selectDiZhu)
                self.appendTouchEvents(self.mySelf.getPointGroup(),self.getPoint,True)
            elif msg['title'] =='显示牌':
                self.appendDisplayEvents(self.showPlayerCard)
                pass
            elif msg['title'] =='出牌':
                self.appendDisplayEvents(self.mySelf.showCard,self.packge.poker[:10])
                self.appendDisplayEvents(self.mySelf.pushCard)
                self.appendTouchEvents(self.mySelf.getPokerGroup(),self.popPoker,True)
                self.appendTouchEvents(self.mySelf.getButtonGroup(),self.pushCard,True)
            elif msg['title'] =='结束':
                self.appendDisplayEvents(self.playerWin,'xx Win')

    # def showPlayerCard(self,data):
    #     #解析
    def playerWin(self,msg):
        font = self.packge.font  # 字体
        text = font.render('%s'%msg, True, (0,0,0))  #显示剩余多少张牌
        self.screen.blit(text,(400,300)) #绘制到屏幕上

    def pushCard(self,sprite):
        poker = []
        for i in self.packge.poker:
            if i.pop:
                poker.append(i.ID)
        print(poker)
        #转换为对应的列表发送出去

    def getPoint(self,sprite):
        point = sprite.point
        print(point)
        # if point == 0:
        #     msg =self.user.convert('point','Y')
        # else:
        #     msg = self.user.convert('point', 'N')
        # self.user.sendMessage(msg)

    def popPoker(self,sprite):
        if sprite.pop ==True:
            sprite.pop =False
        else:
            sprite.pop = True

    def appendTouchEvents(self,spritesGroup,fun,delete=True):
        '''spritesGroup = 精灵组 fun = 要执行的函数 delete事件执行完后是否删除 会将相撞的精灵对象放入到函数中，
        使用函数进行处理即可'''
        def append():
            rect = pygame.sprite.spritecollideany(self.mouse,spritesGroup)
            for sprite in spritesGroup.sprites():
                if rect == sprite.rect:
                    fun(sprite)
            return delete
        self.events['touch'].append(append)

    def appendDisplayEvents(self,fn,data=None):
        def append():
            if data == None:
                fn()
            else:
                fn(data)
        self.events['display'].append(append)

    def gameEvent(self):
        '''处理事件
           请使用装饰器进行重写
        '''
        for event in self.events['display']:
            event()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse.drawPoint()
                for i in self.events['touch']:
                    if i():
                        del self.events['touch'][self.events['touch'].index(i)]

    # 示例
    #         if i.pop == False:
    #             i.pop = True
    #         else:
    #             i.pop = False
    #     if rect == i.rect:
    #         print('图像',i.putCard)
    # def fn(self,sprite):
    #     sprite.pop = True

    def main_loop(self):
        '''流程主循环
           请使用装饰器进行重写
        '''
        while True: #主事件循环
            self.drawBackGroundImage() #背景覆盖
            # self.events.append(self.eventsAppend(self.mySelf.getPokerGroup(),self.fn,True)) #事件添加
            # self.drawOutPokerArea(self.packge.poker[:20])  # 绘制出牌区域
            # self.mySelf.showCard(self.packge.poker[:10])  # 绘制手牌
            # self.rightUser.showCard((self.packge.poker[1:])) # 绘制手牌
            # self.leftUser.showCard((self.packge.poker[1:]))  # 绘制手牌
            # self.mySelf.pushCard()
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
        '''加载资源包'''
        class packge:
            def __init__(self,pygame,settings):
                self.pygame =pygame
                self.settings = settings
                self.poker = [Poker('%s\\%s.jpg' % (self.settings.poker, i), i) for i in range(1, 55)] #加载扑克牌
                self.backgroundImg = pygame.image.load(self.settings.backgroundImage)  # 设置背景
                self.font = pygame.font.SysFont(self.settings.font, 16)  # 加载字体
                self.cardBackGround = pygame.image.load(self.settings.cardBackGround)  # 加载卡牌背景
                self.cardBackGround = pygame.transform.scale(self.cardBackGround, (40, 50))  # 缩放提示牌大小
                point = [self.settings.point0,self.settings.point1,self.settings.point2,self.settings.point3]
                self.points = [Point(point[x],x) for x in range(2)] # 加载叫分图片
                self.pass1 = Buttons(self.settings.pass1,600,360,False) #过图片 精灵类
                self.put = Buttons(self.settings.put,300,360,True)  #出牌 精灵类
                self.putError = pygame.image.load(self.settings.putError) #出牌错误 图片 未用到
                self.putNoCards = pygame.image.load(self.settings.putNoCards)  #没有牌能出 未用到
                self.nongmin = pygame.image.load(self.settings.nongmin) #农民图片
                self.otherDizhu = pygame.image.load(self.settings.otherDizhu) #其他玩家地主图片
                self.otherNongmin = pygame.image.load(self.settings.otherNongmin) #其他玩家农民图片
        print('加载资源包完成')
        return packge(pygame,self.Set)