import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
import glob


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

walkingUp = [
    pygame.image.load('images/boy/boy_up_00.png'),
    pygame.image.load('images/boy/boy_up_01.png'),
    pygame.image.load('images/boy/boy_up_02.png'),
    pygame.image.load('images/boy/boy_up_03.png'),
    pygame.image.load('images/boy/boy_up_04.png'),
    pygame.image.load('images/boy/boy_up_05.png'),
    pygame.image.load('images/boy/boy_up_06.png'),
    pygame.image.load('images/boy/boy_up_07.png'),
    pygame.image.load('images/boy/boy_up_08.png'),
]
walkingLeft = [
    pygame.image.load('images/boy/boy_left_00.png'),
    pygame.image.load('images/boy/boy_left_01.png'),
    pygame.image.load('images/boy/boy_left_02.png'),
    pygame.image.load('images/boy/boy_left_03.png'),
    pygame.image.load('images/boy/boy_left_04.png'),
    pygame.image.load('images/boy/boy_left_05.png'),
    pygame.image.load('images/boy/boy_left_06.png'),
    pygame.image.load('images/boy/boy_left_07.png'),
    pygame.image.load('images/boy/boy_left_08.png'),
]
walkingDown = [
    pygame.image.load('images/boy/boy_down_00.png'),
    pygame.image.load('images/boy/boy_down_01.png'),
    pygame.image.load('images/boy/boy_down_02.png'),
    pygame.image.load('images/boy/boy_down_03.png'),
    pygame.image.load('images/boy/boy_down_04.png'),
    pygame.image.load('images/boy/boy_down_05.png'),
    pygame.image.load('images/boy/boy_down_06.png'),
    pygame.image.load('images/boy/boy_down_07.png'),
    pygame.image.load('images/boy/boy_down_08.png'),
]
walkingRight = [
    pygame.image.load('images/boy/boy_right_00.png'),
    pygame.image.load('images/boy/boy_right_01.png'),
    pygame.image.load('images/boy/boy_right_02.png'),
    pygame.image.load('images/boy/boy_right_03.png'),
    pygame.image.load('images/boy/boy_right_04.png'),
    pygame.image.load('images/boy/boy_right_05.png'),
    pygame.image.load('images/boy/boy_right_06.png'),
    pygame.image.load('images/boy/boy_right_07.png'),
    pygame.image.load('images/boy/boy_right_08.png'),
]
stopUp = 0
stopLeft = 9
stopDown = 18
stopRight = 28

class Boy(pygame.sprite.Sprite):
    def __init__(self, name):
        super(Boy, self).__init__()
        self.walkingUp = glob.glob('images/boy/boy_up*.png')
        self.walkingLeft = glob.glob('images/boy/boy_left*.png')
        self.walkingDown = glob.glob('images/boy/boy_down*.png')
        self.walkingRight = glob.glob('images/boy/boy_right*.png')
        self.walkingUp.sort()
        self.walkingLeft.sort()
        self.walkingDown.sort()
        self.walkingRight.sort()
        self.name = name
        self.walkSpeed = 3
        self.runSpeed = 5
        self.running = False
        self.points = 0
        self.health = 100
        self.alive = True
        self.pos = 0
        self.pos_max = 8
        self.img = pygame.image.load(self.walkingDown[self.pos])
        self.rect = self.img.get_rect()
        self.rect.center = (200,300)

    def hit(self, enemy):
        self.health -= enemy.dmg
        if self.health <= 0:
            self.alive = False
    
    def addPoints(self, point):
        self.points += point

    def removePoints(self, point):
        self.points -+ point

    def update(self, direction):
        if direction == UP:
            self.rect.move_ip(0, -self.walkSpeed)
            self.img = pygame.image.load(self.walkingUp[self.pos])
            if self.pos == self.pos_max:
                self.pos = 1
            else:
                self.pos += 1
        elif direction == DOWN:
            self.rect.move_ip(0, self.walkSpeed)
            self.img = pygame.image.load(self.walkingDown[self.pos])
            if self.pos == self.pos_max:
                self.pos = 1
            else:
                self.pos += 1
        elif direction == LEFT:
            self.rect.move_ip(-self.walkSpeed, 0)
            self.img = pygame.image.load(self.walkingLeft[self.pos])
            if self.pos == self.pos_max:
                self.pos = 1
            else:
                self.pos += 1
        elif direction == RIGHT:
            self.rect.move_ip(self.walkSpeed, 0)
            self.img = pygame.image.load(self.walkingRight[self.pos])
            if self.pos >= self.pos_max:
                self.pos = 1
            else:
                self.pos += 1
            