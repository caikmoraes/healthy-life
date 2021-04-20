import pygame
from pygame.locals import *
import sys
import time
import pyganim

pygame.init()

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Game screen size
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Characters sprites
boy_stop_right = pygame.image.load("assets/img/boy_stop.png").convert_alpha()
girl_stop_right = pygame.image.load("assets/img/girl_stop.png").convert_alpha()
boy_stop_left = pygame.transform.flip(boy_stop_right, True, False)

boyWidth, boyHeight = boy_stop_right.get_size()

animTypes = 'right_run right_walk'.split()
animObjs = {}
for type in animTypes:
    imgAndAnimation = [('assets/img/boy_%s.%s.png' % (type, str(num).rjust(2, '0')), 0.1) for num in range(2)]
    animObjs[type] = pyganim.PygAnimation(imgAndAnimation)

animObjs['left_walk'] = animObjs['right_walk'].getCopy()
animObjs['left_walk'].flip(True, False)
animObjs['left_walk'].makeTransformsPermanent()
animObjs['left_run'] = animObjs['right_run'].getCopy()
animObjs['left_run'].flip(True, False)
animObjs['left_run'].makeTransformsPermanent()

moveBoy = pyganim.PygConductor(animObjs)

direction = RIGHT
BGCOLOR = (100, 50, 50)
mainClock = pygame.time.Clock()
x = 300 # x and y are the player's position
y = 200
WALKRATE = 2
RUNRATE = 4