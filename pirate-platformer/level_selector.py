import pygame
from settings import *
from class_Button import Button
import os

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

level_1_button = Button(
    SCREEN_WIDTH // 2 - 350, SCREEN_HEIGHT // 2, level_1_btn, screen)
level_2_button = Button(SCREEN_WIDTH // 2 - 70,
                        SCREEN_HEIGHT // 2, level_2_btn, screen)
level_3_button = Button(SCREEN_WIDTH // 2 + 200,
                        SCREEN_HEIGHT // 2, level_3_btn, screen)

pygame.font.init()
font = pygame.font.SysFont("Arial", 34)


def level_selector():
    """
    Función que maneja el menú principal del juego.

    Esta función maneja la pantalla de menú principal del juego. Muestra botones para jugar, ver las instrucciones y salir del juego. Detecta eventos de clics y teclas para permitir al usuario interactuar con el menú.
    """
    clock = pygame.time.Clock()
    running = True
    contador_de_clicks = 0

    while running:
        screen.blit(bkg_image, (0, 0))
        clock.tick(FPS)
        # Dibujo título principal
        texto_titulo = "*Pirate Platforms - Menu*"
        if level_1_button.draw():
            level = 1
            return level
        if level_2_button.draw():
            level = 2
            return level
            print(options_menu)
        if level_3_button.draw():
            level = 3
            return level
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

        pygame.display.update()

level_selector()
    
pygame.quit()
