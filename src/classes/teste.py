import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

surf = pygame.image.load('../images/walk.png').convert_alpha()

def getFrame(gid):
    columns = 9
    width = 64
    height = 62
    margin = 0
    top = 0
    line = gid // columns
    col = gid % columns
    space_v = 0
    space_h = 0
    x = (col  * (width + space_h)) + margin
    y = (line  * (height + space_v)) + top
    quadro = surf.subsurface(Rect((x,y), (width, height)))
    return quadro

walkingLeft = [10,11,12,13,14,15,16,17]
walkingRight = [28,29,30,31,32,33,34,35]

lista_quadro = walkingLeft

quadro = 0

clock = pygame.time.Clock()

while True:

    screen.fill((100,100,100))
    gid = lista_quadro[quadro]
    frame = getFrame(gid)
    quadro += 1
    if quadro > len(lista_quadro):
        quadro = 0
    screen.blit(frame, (400, 300))
    pygame.display.update()
    clock.tick(10)