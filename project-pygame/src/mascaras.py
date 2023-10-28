import pygame
from aleatorias import generate_random_color, get_random_direction, create_blocks
from random import randint, randrange
from pygame.time import Clock
from config import *
from pygame.locals import *
from colisiones import *
from utils import *


# inicializar los modulos de pygame
pygame.init()

# config de la pantalla principal
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mascaras")

player = pygame.transform.scale(pygame.image.load(), (200, 200))
rect_player = player.get_rect()
mask_player = pygame.mask.from_surface(player)

asteroid = pygame.transform.scale(pygame.image.load(), (200, 200))
rect_asteroid = asteroid.get_rect()
rect_asteroid.center = CENTER_SCREEN
mask_asteroid = pygame.mask.from_surface(asteroid)


running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEMOTION:
            if event.button == 1:
                rect_player.center = event.pos

    offset = (rect_asteroid.x - rect_player.x, rect_asteroid.y - rect_player.y)
    if mask_player.overlap(mask_asteroid, offset) != None:
        # colision
        pass

    screen.fill(black)

    screen.blit(asteroid, rect_asteroid)

    screen.blit(player, rect_player)

    pygame.display.flip


pygame.quit()
exit()
