import pygame
import random
import glob

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

foodImgs = glob.glob('images/foods/fat_food*.png')

class FatFood(pygame.sprite.Sprite):
    def __init__(self):
        super(FatFood, self).__init__()
        icon = random.randint(0,3)
        iconImg = pygame.image.load(foodImgs[icon])
        self.dmg = 5 + icon
        self.speed = random.randint(5, 10)
        self.img = pygame.transform.scale(iconImg, (32, 32))
        self.rect = self.img.get_rect()
        self.rect.center = (
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 40),
            random.randint(SCREEN_HEIGHT - 420, SCREEN_HEIGHT - 210) 
        )

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()