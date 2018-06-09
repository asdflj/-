class Settings:
    def __init__(self):
        self.images= "images\\"
        self.backgroundImage = self.images+'background.png'
        self.nongmin = self.images + 'nongming.png'
        self.poker = ['%spoker\\%s.jpg'%(self.images,i) for i in range(1,55)]
        self.otherNongmin = self.images + 'nongmin.bmp'
        self.dizhu = self.images + 'humantype2win.bmp'
        self.otherDizhu = self.images + 'humantype2.png'