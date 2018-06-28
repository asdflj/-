class Settings:
    def __init__(self):
        self.images= "images\\"
        self.backgroundImage = self.images+'background.png'
        self.nongmin = self.images + 'nongming.png'
        self.poker = self.images+'poker'
        self.otherNongmin = self.images + 'nongmin.bmp'
        self.dizhu = self.images + 'humantype2win.bmp'
        self.otherDizhu = self.images + 'humantype2.png'
        self.screenWidth = 1000
        self.screenHeight = 600
        self.cardBackGround = self.images+'cardbg.png'
        self.point3 = self.images+'point3.png'
        self.point0 = self.images+'point0.png'
        self.point1 = self.images+'point1.png'
        self.point2 = self.images+'point2.png'
        self.font = r'font\jyzt.ttf'
        self.pass1 = self.images+'pass.png'
        self.put = self.images+'put.png'
        self.putError = self.images +'notify_rule.png'
        self.putNoCards = self.images +'no_put_cards.png'

        ##################扑克基础属性################
        self.pokerInterval = 105  #扑克标准间隔
        self.pokerWidth = 150 #扑克标准宽度
        #############################################

        self.bottomCardsX = 250 #底牌显示位置
        self.bottomCardsY = 20 #底牌显示位置

        self.outPokerAreaWidth = 700 #出牌区域宽度
        self.outPokerCardsX = 120
        self.outPokerCardsY = 200
