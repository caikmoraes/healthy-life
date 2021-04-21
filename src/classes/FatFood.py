import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class FatFood(pygame.sprite.Sprite):
    def __init__(self):
        super(FatFood, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 40),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()