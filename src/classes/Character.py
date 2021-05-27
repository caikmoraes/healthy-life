import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"



class Character(pygame.sprite.Sprite):
    def __init__(self, name, walkingUp, walkingLeft, walkingDown, walkingRight):
        super(Character, self).__init__()
        self.walkingUp = walkingUp
        self.walkingLeft = walkingLeft
        self.walkingDown = walkingDown
        self.walkingRight = walkingRight
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
        self.rect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + 20)
        self.max_pontuation = 0
        self.high_level = 1
        self.current_level = 1

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
                if not self.rect.right >= SCREEN_WIDTH/2 + 100:
                    self.rect.move_ip(self.runSpeed, 0)

        else:
            if direction == UP:
                if self.rect.left <= 317 and self.rect.bottom <= 375:
                    # self.rect.move_ip(0, -self.walkSpeed)
                    self.img = pygame.image.load(self.walkingUp[self.pos])
                    
                elif not self.rect.bottom <= 340:
                    self.rect.move_ip(0, -self.walkSpeed)
                    self.img = pygame.image.load(self.walkingUp[self.pos])
                    if self.pos == self.pos_max:
                        self.pos = 1
                    else:
                        self.pos += 1
            elif direction == DOWN:
                if not self.rect.bottom >= SCREEN_HEIGHT - 150:
                    self.rect.move_ip(0, self.walkSpeed)
                    self.img = pygame.image.load(self.walkingDown[self.pos])
                    if self.pos == self.pos_max:
                        self.pos = 1
                    else:
                        self.pos += 1
            elif direction == LEFT:
                if not self.rect.bottom <= 335 and not self.rect.left <= 330:
                    self.rect.move_ip(-self.walkSpeed, 0)
                    self.img = pygame.image.load(self.walkingLeft[self.pos])
                    if self.pos == self.pos_max:
                        self.pos = 1
                    else:
                        self.pos += 1
                elif self.rect.bottom >= 373 and not self.rect.left < 250:
                    self.rect.move_ip(-self.walkSpeed, 0)
                    self.img = pygame.image.load(self.walkingLeft[self.pos])
                    if self.pos == self.pos_max:
                        self.pos = 1
                    else:
                        self.pos += 1
            elif direction == RIGHT:
                if not self.rect.right >= SCREEN_WIDTH - 235:
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

    def next_level(self):
        self.current_level += 1
        self.increase_health()

    def set_high_level(self):
        if self.current_level > self.high_level:
            self.high_level = self.current_level
    
    def increase_health(self):
        if self.current_level % 2 == 0:
            self.health += 10
            if self.health >= 100:
                self.health = 100