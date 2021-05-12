from classes.Levels import Level
from random import random
import pygame
import pygame_menu
from pygame_menu.controls import KEY_CLOSE_MENU
from classes.Girl import Girl
from pygame.locals import *
from classes.Boy import Boy
from classes.FatFood import FatFood
from classes.HalthyFood import HealthyFood
from classes.GameCam import GameCam
import random
import os

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

HOME = pygame.image.load('images/scene/casa.jpeg')
FLOREST = pygame.image.load('images/scene/floresta.jpeg')

pygame.display.set_caption("Healthy-Life")

clock = pygame.time.Clock()

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
gaming_song = pygame.mixer.Sound(os.path.join('sounds', 'gaming.ogg'))
home_song = pygame.mixer.Sound(os.path.join('sounds', 'home.ogg'))
running_song = pygame.mixer.Sound(os.path.join('sounds', 'running.ogg'))
gameover_song = pygame.mixer.Sound(os.path.join('sounds', 'gameover.ogg'))

sound_on = True

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

def show_current_level(c):
    level = BASICFONT.render('Nível: %d' % c.current_level, True, (255,255,255))
    level_rect = level.get_rect()
    level_rect.bottomleft = (SCREEN_WIDTH/2, SCREEN_HEIGHT - (SCREEN_HEIGHT - 100))
    SCREEN.blit(level, level_rect)

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
                menu.add.label('%s --> Pontos: %d --> Nível: %d' % (p.name, p.max_pontuation, p.high_level))

        menu.add.button('Voltar', action=main_menu)
        menu.mainloop(ranking_screen)
    

def show_instructions():
    # Necessita criar instruções
    pass

gender = ''
def set_gender(key, value):
    global gender
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
    global sound_on
    if value == 1:
        sound_on = True
    else:
        sound_on = False
    play_music_by_env('menu')
    pass

def play_music_by_env(env):
    global home_song
    global running_song
    global gameover_song
    global gaming_song
    global sound_on
    if not sound_on:
        home_song.stop()
        running_song.stop()
        gameover_song.stop()
        gaming_song.stop()
    else:    
        home_song.stop()
        running_song.stop()
        gameover_song.stop()
        gaming_song.stop()
        if env == 'home':
            home_song.play()
        elif env == 'florest':
            running_song.play()
        elif env == 'menu':
            gaming_song.play()
        elif env == 'gameover':
            gameover_song.play()
        

def home():
    play_music_by_env('home')
    walkLeft = walkUp = walkRight = walkDown = False
    if gender == 1:
        character = Boy(characterName)
    elif gender == 2:
        character = Girl(characterName)
    players.append(character)

    inHome = True
    room = pygame.transform.scale(HOME, (600,400))
    while inHome:
        character.running = False
        clock.tick(30)
        SCREEN.fill((0,0,0))
        SCREEN.blit(room, (SCREEN.get_rect()))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
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

        if character.rect.top > SCREEN_HEIGHT - 250:
            game(character)
            

        pygame.display.flip()

def game(character):
    play_music_by_env('florest')
    camera = GameCam(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    off_camera = GameCam(SCREEN_WIDTH+SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    cameras = pygame.sprite.Group()
    cameras.add(camera)
    cameras.add(off_camera)
    level_health = Level(True)
    level_fat = Level(False)
    levels = [level_health, level_fat]
    walkLeft = walkUp = walkRight = walkDown = False
    character.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    running = True
    character.running = running
    fat_timer = 1000
    health_timer = 1100
    direction = DOWN
    fatFoods = pygame.sprite.Group()
    healthyFoods = pygame.sprite.Group()
    gameSprites = pygame.sprite.Group()
    gameSprites.add(character)
    ADD_FATFOOD = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_FATFOOD, fat_timer)
    ADD_HEALTHYFOOD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADD_HEALTHYFOOD, health_timer)
    ADD_POINTS = pygame.USEREVENT + 3
    pygame.time.set_timer(ADD_POINTS, 500)
    SET_ANIMATION = pygame.USEREVENT + 4
    pygame.time.set_timer(SET_ANIMATION, 35)
    NEXT_LEVEL = pygame.USEREVENT + 5
    pygame.time.set_timer(NEXT_LEVEL, 10000)

    while running:
        clock.tick(30)
        for cam in cameras:
            SCREEN.blit(cam.img, cam.rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    home()
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
            elif event.type == NEXT_LEVEL:
                if character.alive:
                    character.next_level()
                    for level in levels:
                        level.set_timer()
                        if level.is_health:
                            health_timer += level.timer
                        else:
                            fat_timer += level.timer

        cameras.update()

        if walkRight or walkDown or walkLeft or walkUp:
            character.update(direction)

        fatFoods.update()
        healthyFoods.update()

        if not character.alive:
            character.new_record()
            character.kill()
            gameover()
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

        show_current_level(character)

        pygame.display.flip()

def gameover():
    play_music_by_env('gameover')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    home()
        
        gameOver = BASICFONT.render('GAME OVER. Pressione ESC para ir para o quarto.', True, (255,50,50))
        gameOverRect = gameOver.get_rect()
        gameOverRect.bottomleft = (SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/2)
        SCREEN.blit(gameOver, gameOverRect)
        pygame.display.flip()

def main_menu():
    play_music_by_env('menu')
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