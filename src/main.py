import pygame
from pygame.locals import *
from classes.Boy import Boy
from classes.FatFood import FatFood
from classes.HalthyFood import HealthyFood

pygame.init()


# Game screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

BASICFONT = pygame.font.Font('freesansbold.ttf', 16)



pygame.display.set_caption("Healthy-Life")

# Imagem personagens parados

boy = Boy('Caik')

fatFoods = pygame.sprite.Group()
healthyFoods = pygame.sprite.Group()
gameSprites = pygame.sprite.Group()
gameSprites.add(boy)

ADD_FATFOOD = pygame.USEREVENT + 1
ADD_HEALTHYFOOD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_FATFOOD, 500)
pygame.time.set_timer(ADD_HEALTHYFOOD, 500)

ADD_POINTS = pygame.USEREVENT + 3
pygame.time.set_timer(ADD_POINTS, 500)


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
            fatFoods.add(newFatFood)
            gameSprites.add(newFatFood)
        elif event.type == ADD_HEALTHYFOOD:
            newHealthyFood = HealthyFood()
            healthyFoods.add(newHealthyFood)
            gameSprites.add(newHealthyFood)
        elif event.type == ADD_POINTS:
            if boy.alive:
                boy.addPoints(1)


    key = pygame.key.get_pressed()
    boy.update(key)
    fatFoods.update()
    healthyFoods.update()


    if not boy.alive:
        boy.kill()
        gameOver = BASICFONT.render('GAME OVER.', True, (255,50,50))
        gameOverRect = gameOver.get_rect()
        gameOverRect.bottomleft = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        SCREEN.blit(gameOver, gameOverRect)
    else:
        for sprite in gameSprites:
            SCREEN.blit(sprite.surf, sprite.rect)

        for food in healthyFoods:
            if pygame.sprite.collide_rect(food, boy):
                boy.addPoints(30)
                food.kill()

        for food in fatFoods:
            if pygame.sprite.collide_rect(food, boy):
                boy.removePoints(20)
                boy.hit()
                food.kill()



    pointLegend = BASICFONT.render('Pontos: %d' % boy.points, True, (255,255,255))
    pointRect = pointLegend.get_rect()
    pointRect.bottomleft = (10, SCREEN_HEIGHT - 10)
    SCREEN.blit(pointLegend, pointRect)

    healthLegend = BASICFONT.render('Saúde: %d' % boy.health, True, (255,255,255))
    healthRect = healthLegend.get_rect()
    healthRect.bottomleft = (10, SCREEN_HEIGHT - 30)
    SCREEN.blit(healthLegend, healthRect)

    pygame.display.flip()