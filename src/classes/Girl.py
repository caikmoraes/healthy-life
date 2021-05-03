import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
import glob


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"


class Girl(pygame.sprite.Sprite):
    def __init__(self, name):
        super(Girl, self).__init__()
        self.walkingUp = glob.glob('images/girl/girl_up*.png')
        self.walkingLeft = glob.glob('images/girl/girl_left*.png')
        self.walkingDown = glob.glob('images/girl/girl_down*.png')
        self.walkingRight = glob.glob('images/girl/girl_right*.png')
        self.walkingUp.sort()
        self.walkingLeft.sort()
        self.walkingDown.sort()
        self.walkingRight.sort()
        self.name = name
        self.walkSpeed = 3
        self.runSpeed = 6
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

    def update(self, direction):
        if self.running:
            if direction == UP:
                self.rect.move_ip(0, -self.runSpeed)
                self.img = pygame.image.load(self.walkingUp[self.pos])
                if self.pos == self.pos_max:
                    self.pos = 1
                else:
                    self.pos += 1
            elif direction == DOWN:
                self.rect.move_ip(0, self.runSpeed)
                self.img = pygame.image.load(self.walkingDown[self.pos])
                if self.pos == self.pos_max:
                    self.pos = 1
                else:
                    self.pos += 1
            elif direction == LEFT:
                self.rect.move_ip(-self.runSpeed, 0)
                self.img = pygame.image.load(self.walkingLeft[self.pos])
                if self.pos == self.pos_max:
                    self.pos = 1
                else:
                    self.pos += 1
            elif direction == RIGHT:
                self.rect.move_ip(self.runSpeed, 0)
                self.img = pygame.image.load(self.walkingRight[self.pos])
                if self.pos >= self.pos_max:
                    self.pos = 1
                else:
                    self.pos += 1
        else:
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