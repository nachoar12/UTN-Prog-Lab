import pygame
from aleatorias import generate_random_color, get_random_direction, create_blocks
from random import randint, randrange
from pygame.time import Clock
from config import *
from pygame.locals import *
from colisiones import *
from utils import *

background_color_button = magenta
background_color_button_hover = yellow

# inicializar los modulos de pygame
pygame.init()

# config de la pantalla principal
pygame.display.set_caption("Menu Principal")
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((white))

rect_saludar = pygame.Rect(100, 100, 200, 30)
rect_brindar = pygame.Rect(100, 160, 200, 50)
rect_despedir = pygame.Rect(100, 220, 200, 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                # coordenads donde se hizo click en la pantalla
                cursor = event.pos

                if rect_saludar.collidepoint(cursor[0], cursor[1]):
                    print("Hola mundo")
                elif rect_brindar.collidepoint(cursor[0], cursor[1]):
                    print("Chin chin...")
                elif rect_despedir.collidepoint(cursor[0], cursor[1]):
                    print("Cerrando programa...")
                    running = False

    screen.fill(black)

    crear_boton(screen, rect_saludar, "Saludar",
                background_color_button, background_color_button_hover)
    crear_boton(screen, rect_saludar, "Brindar",
                background_color_button, background_color_button_hover)
    crear_boton(screen, rect_saludar, "Despedir",
                background_color_button, background_color_button_hover)

    pygame.display.flip


pygame.quit()
exit()
