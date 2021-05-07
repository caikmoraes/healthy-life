from random import random
import pygame
import pygame_menu
from pygame_menu.controls import KEY_CLOSE_MENU
from classes.Girl import Girl
from pygame.locals import *
from classes.Boy import Boy
from classes.FatFood import FatFood
from classes.HalthyFood import HealthyFood
import random

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

clock = pygame.time.Clock()

players = []

ranking = True

def show_points(c):
    pointLegend = BASICFONT.render('Pontos: %d' % c.points, True, (255,255,255))
    pointRect = pointLegend.get_rect()
    pointRect.bottomleft = (10, SCREEN_HEIGHT - 10)
    SCREEN.blit(pointLegend, pointRect)

def show_health(c):
    bar_width= 100
    bar_height= 10
    healthLegend = BASICFONT.render('Saúde:', True, (255,255,255))
    legend_width = healthLegend.get_width()
    health_bar = pygame.Rect(legend_width + 20, SCREEN_HEIGHT - 43, c.health, bar_height)
    background_bar = pygame.Rect(legend_width + 20, SCREEN_HEIGHT - 43, bar_width, bar_height)
    healthRect = healthLegend.get_rect()
    healthRect.bottomleft = (10, SCREEN_HEIGHT - 30)
    SCREEN.blit(healthLegend, healthRect)
    pygame.draw.rect(SCREEN, (100,100,100), background_bar)
    pygame.draw.rect(SCREEN, (200,0,0), health_bar)

def close_ranking():
    global ranking
    ranking = False
    pass

def order_ranking(player):
    return player.max_pontuation

def show_ranking():
    global players
    players.sort(key= order_ranking, reverse=True)
    while True:
        ranking_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        menu = pygame_menu.Menu(500, 500, 'Ranking',theme=pygame_menu.themes.THEME_ORANGE)
        if len(players) <= 0:
            menu.add.label('Sem jogadores cadastrados')
        else:
            for p in players:
                menu.add.label('%s --> %d' % (p.name, p.max_pontuation))

        menu.add.button('Voltar', action=main_menu)
        menu.mainloop(ranking_screen)
    

def show_instructions():
    # Necessita criar instruções
    pass

gender = ''
def set_gender(key, value):
    global gender
    print(value)
    gender = value
    pass

characterName = ''
def set_name(name):
    global characterName
    if name == '' or name == None:
        name = 'visitante%d' % random.randint(0, 100)
    characterName = name
    pass

def set_music(key, value):
    # Do the job here !
    pass

def home():
    walkLeft = walkUp = walkRight = walkDown = False
    if gender == 1:
        character = Boy(characterName)
    elif gender == 2:
        character = Girl(characterName)
    players.append(character)

    inHome = True
    while inHome:
        character.running = False
        clock.tick(30)
        SCREEN.fill((80,80,80))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    inHome = False
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

        if walkRight or walkDown or walkLeft or walkUp:
            character.update(direction)

        SCREEN.blit(character.img, character.rect)

        if character.rect.top > SCREEN_HEIGHT:
            game(character)

        pygame.display.flip()

def game(character):
    walkLeft = walkUp = walkRight = walkDown = False
    character.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    running = True
    character.running = running

    direction = DOWN
    fatFoods = pygame.sprite.Group()
    healthyFoods = pygame.sprite.Group()
    gameSprites = pygame.sprite.Group()
    gameSprites.add(character)
    ADD_FATFOOD = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_FATFOOD, 500)
    ADD_HEALTHYFOOD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADD_HEALTHYFOOD, 500)
    ADD_POINTS = pygame.USEREVENT + 3
    pygame.time.set_timer(ADD_POINTS, 500)
    SET_ANIMATION = pygame.USEREVENT + 4
    pygame.time.set_timer(SET_ANIMATION, 35)
    while running:
        
        clock.tick(30)
        SCREEN.fill((80,80,80))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
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
                if character.alive:
                    character.addPoints(1)
            elif event.type == SET_ANIMATION:
                character.next_animation()


        if walkRight or walkDown or walkLeft or walkUp:
            character.update(direction)

        fatFoods.update()
        healthyFoods.update()

        if not character.alive:
            character.new_record()
            character.kill()
            gameOver = BASICFONT.render('GAME OVER. Pressione ESC para ir para o quarto.', True, (255,50,50))
            gameOverRect = gameOver.get_rect()
            gameOverRect.bottomleft = (SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/2)
            SCREEN.blit(gameOver, gameOverRect)
        else:
            for sprite in gameSprites:
                SCREEN.blit(sprite.img, sprite.rect)

            for food in healthyFoods:
                if pygame.sprite.collide_rect(food, character):
                    character.addPoints(food.points)
                    food.kill()

            for food in fatFoods:
                if pygame.sprite.collide_rect(food, character):
                    character.hit(food)
                    food.kill()



        show_points(character)

        show_health(character)

        pygame.display.flip()


def main_menu():
    while True:
        menu = pygame_menu.Menu(500, 500, 'Healthy Life',theme=pygame_menu.themes.THEME_ORANGE)
        menu.add.text_input('Nome: ', onchange=set_name, )
        menu.add.selector('Sexo: ', [('Masculino',1), ('Feminino',2)], onchange=set_gender, default=1)
        menu.add.selector('Som: ', [('Ligado', 1), ('Desligado', 2)], onchange=set_music)
        menu.add.button('Instruções', show_instructions)
        menu.add.button('Jogar', home)
        menu.add.button('Ranking', show_ranking)
        menu.add.button('Sair', pygame_menu.events.EXIT)
        menu.mainloop(SCREEN)

if __name__ == "__main__":
    main_menu()