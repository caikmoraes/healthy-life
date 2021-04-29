import pygame
from pygame.locals import *
from classes.Boy import Boy
from classes.FatFood import FatFood
from classes.HalthyFood import HealthyFood

pygame.init()

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

# Game screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

BASICFONT = pygame.font.Font('freesansbold.ttf', 16)



pygame.display.set_caption("Healthy-Life")


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

walkLeft = walkUp = walkRight = walkDown = False

direction = DOWN

while True:
    clock.tick(30)
    SCREEN.fill((80,80,80))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            if event.key == K_LSHIFT:
                boy.running = True
            if event.key == K_LEFT:
                walkLeft = True
                walkRight = False
                if not walkUp and not walkDown:
                    direction = LEFT
            if event.key == K_UP:
                walkUp = True
                walkDown = False
                if not walkLeft and not walkRight:
                    direction = UP
            if event.key == K_DOWN:
                walkDown = True
                walkUp = False
                if not walkLeft and not walkRight:
                    direction = DOWN
            if event.key == K_RIGHT:
                walkRight = True
                walkLeft = False
                if not walkUp and not walkDown:
                    direction = RIGHT
        elif event.type == KEYUP:
            if event.key == K_LSHIFT:
                boy.running = False
            if event.key == K_UP:
                walkUp = False
                if walkLeft:
                    direction = LEFT
                if walkRight:
                    direction = RIGHT
            elif event.key == K_DOWN:
                walkDown = False
                if walkLeft:
                    direction = LEFT
                if walkRight:
                    direction = RIGHT
            elif event.key == K_LEFT:
                walkLeft = False
                if walkUp:
                    direction = UP
                if walkDown:
                    direction = DOWN
            elif event.key == K_RIGHT:
                walkRight = False
                if walkUp:
                    direction = UP
                if walkDown:
                    direction = DOWN
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


    if walkRight or walkDown or walkLeft or walkUp:
        boy.update(direction)


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
            SCREEN.blit(sprite.img, sprite.rect)

        for food in healthyFoods:
            if pygame.sprite.collide_rect(food, boy):
                boy.addPoints(food.points)
                food.kill()

        for food in fatFoods:
            if pygame.sprite.collide_rect(food, boy):
                boy.hit(food)
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