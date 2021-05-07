import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
import glob


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"



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
        self.max_pontuation = 0

    def new_record(self):
        if self.points > self.max_pontuation:
            self.max_pontuation = self.points

    def hit(self, enemy):
        self.health -= enemy.dmg
        if self.health <= 0:
            self.alive = False
    
    def addPoints(self, point):
        self.points += point

    def update(self, direction):
        if self.running:
            if direction == UP:
                if not self.rect.bottom <= SCREEN_HEIGHT - 420:
                    self.rect.move_ip(0, -self.runSpeed)


            elif direction == DOWN:
                if not self.rect.bottom >= SCREEN_HEIGHT - 210:
                    self.rect.move_ip(0, self.runSpeed)

            elif direction == LEFT:
                if not self.rect.left <= 5:
                    self.rect.move_ip(-self.runSpeed, 0)

            elif direction == RIGHT:
                if not self.rect.right >= SCREEN_WIDTH/2:
                    self.rect.move_ip(self.runSpeed, 0)

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
                
    def next_animation(self):
        self.img = pygame.image.load(self.walkingRight[self.pos])
        if self.pos >= self.pos_max:
            self.pos = 1
        else:
            self.pos += 1