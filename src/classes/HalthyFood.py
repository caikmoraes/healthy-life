import pygame
import random
import glob

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

foodImgs = glob.glob('images/foods/healthy_food*.png')

class HealthyFood(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthyFood, self).__init__()
        icon = random.randint(0,2)
        iconImg = pygame.image.load(foodImgs[icon])
        self.speed = random.randint(5, 10)
        self.img = pygame.transform.scale(iconImg, (32, 32))
        self.points = 20 + icon
        self.rect = self.img.get_rect()
        self.rect.center = (
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 40),
            random.randint(0, SCREEN_HEIGHT) 
        )

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()