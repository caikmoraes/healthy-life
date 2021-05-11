import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

floresta = pygame.image.load('images/scene/floresta.jpeg')

class GameCam(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(GameCam, self).__init__()
        self.img = pygame.transform.scale(floresta, (800, 600))
        self.rect = self.img.get_rect()
        self.rect.center = (pos_x,pos_y)

    def update(self):
        self.rect.move_ip(-10, 0)
        if(self.rect.right <= 0):
           self.rect.center = (SCREEN_WIDTH+SCREEN_WIDTH/2,SCREEN_HEIGHT/2) 