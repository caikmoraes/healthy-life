import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Boy(pygame.sprite.Sprite):
    def __init__(self, name):
        super(Boy, self).__init__()
        self.surf = pygame.Surface((75,75))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH,
                SCREEN_HEIGHT/2
            )
        )
        self.name = name
        self.walkSpeed = 5
        self.runSpeed = 10
        self.running = False
        self.points = 0
        self.health = 100
        self.alive = True

    def hit(self):
        self.health -= 5
        if self.health <= 0:
            self.alive = False
    
    def addPoints(self, point):
        self.points += point

    def removePoints(self, point):
        self.points -+ point

    def update(self, direction):
        if self.running:
            if direction[K_UP]:
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