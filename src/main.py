import pygame
from pygame.locals import *
from classes.Boy import Boy
from classes.FatFood import FatFood
from classes.HalthyFood import HealthyFood

pygame.init()

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Game screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pygame.display.set_caption("Healthy-Life")

# Imagem personagens parados
boy_stop_right = pygame.image.load("assets/img/boy_stop.png").convert_alpha()
girl_stop_right = pygame.image.load("assets/img/girl_stop.png").convert_alpha()
boy_stop_left = pygame.transform.flip(boy_stop_right, True, False)
girl_stop_left = pygame.transform.flip(girl_stop_right, True, False)

boy = Boy('Caik')

foods = pygame.sprite.Group()
gameSprites = pygame.sprite.Group()
gameSprites.add(boy)

ADD_FATFOOD = pygame.USEREVENT + 1
ADD_HEALTHYFOOD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_FATFOOD, 350)
pygame.time.set_timer(ADD_HEALTHYFOOD, 350)

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    SCREEN.fill((80,80,80))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            if event.key == K_LSHIFT:
                boy.running = True
        elif event.type == KEYUP:
            if event.key == K_LSHIFT:
                boy.running = False
        elif event.type == ADD_FATFOOD:
            newFatFood = FatFood()
            foods.add(newFatFood)
            gameSprites.add(newFatFood)
        elif event.type == ADD_HEALTHYFOOD:
            newHealthyFood = HealthyFood()
            foods.add(newHealthyFood)
            gameSprites.add(newHealthyFood)


    boy.update(pygame.key.get_pressed())
    foods.update()

    for sprite in gameSprites:
        SCREEN.blit(sprite.surf, sprite.rect)

    pygame.display.flip()