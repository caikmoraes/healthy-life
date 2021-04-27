import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP


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
        self.walkingUp = walkingUp
        self.walkingLeft = walkingLeft
        self.walkingDown = walkingDown
        self.walkingRight = walkingRight
        self.name = name
        self.walkSpeed = 3
        self.runSpeed = 5
        self.running = False
        self.points = 0
        self.health = 100
        self.alive = True
        self.index = 0
        self.image = self.walkingDown[self.index]
        self.rect = self.image.get_rect()
        self.surf = pygame.Surface((20, 10))
    

    def hit(self):
        self.health -= 5
        if self.health <= 0:
            self.alive = False
    
    def addPoints(self, point):
        self.points += point

    def removePoints(self, point):
        self.points -+ point

    def update(self, direction):
        self.index += 1
        if self.running:
            if direction[K_UP]:
                if self.index >= len(self.walkingUp):
                    self.index = 1
                self.rect.move_ip(0, -self.runSpeed)
            elif direction[K_DOWN]:
                self.rect.move_ip(0, self.runSpeed)
            elif direction[K_LEFT]:
                self.rect.move_ip(-self.runSpeed, 0)
            elif direction[K_RIGHT]:
                self.rect.move_ip(self.runSpeed, 0)
        else:
            if direction[K_UP]:
                self.rect.move_ip(0, -self.walkSpeed)
            elif direction[K_DOWN]:
                self.rect.move_ip(0, self.walkSpeed)
            elif direction[K_LEFT]:
                self.rect.move_ip(-self.walkSpeed, 0)
            elif direction[K_RIGHT]:
                self.rect.move_ip(self.walkSpeed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH/2:
            self.rect.right = SCREEN_WIDTH/2
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT