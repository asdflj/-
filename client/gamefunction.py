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
        super().__init__(pygame,image,screen)
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        self.rect.x = 50     #设置位置
        self.rect.y = 450
    def showCard(self,Puker):
        pass
        # for i in Puker:
            # image = self.pygame.image.load()

class PLeft(Player):
    def __init__(self,pygame,image,screen):
        super().__init__(pygame,image,screen)
        self.image = self.pygame.transform.rotate(self.image,-130)
        self.rect.x = 0     #设置位置
        self.rect.y = -15

class PRight(Player):
    def __init__(self,pygame,image,screen):
        super().__init__(pygame,image,screen)
        self.image = self.pygame.transform.rotate(self.image,130)
        self.rect.x = 810     #设置位置
        self.rect.y = -15

