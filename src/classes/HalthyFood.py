import pygame
import random
import glob

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

foodImgs = glob.glob('images/foods/healthy_food*.png')
img = pygame.image.load(foodImgs[0])
test_img = pygame.transform.scale(img, (32, 32))

class HealthyFood(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthyFood, self).__init__()
        self.speed = random.randint(5, 10)
        self.img = test_img
        self.rect = self.img.get_rect()
        self.rect.center = (
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 40),
            random.randint(0, SCREEN_HEIGHT) 
        )

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()