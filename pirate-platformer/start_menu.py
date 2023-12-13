import pygame
from settings import *
from class_Button import Button
from level_selector import level_selector

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

start_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2 - 100, start_btn, screen)
options_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2, options_btn, screen)
exit_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2 + 100, exit_btn, screen)

pygame.font.init()
font = pygame.font.SysFont("Arial", 34)

def start_menu():
    """
    Función que maneja el menú principal del juego.

    Esta función maneja la pantalla de menú principal del juego. Muestra botones para jugar, ver las instrucciones y salir del juego. Detecta eventos de clics y teclas para permitir al usuario interactuar con el menú.
    """
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(bkg_image, (0, 0))
        clock.tick(FPS)
        if exit_button.draw():
            running = False
        if options_button.draw():
            options_menu = 1
            return
            print(options_menu)
        if start_button.draw():
            level_selector()
            return
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

        pygame.display.update()

start_menu()

pygame.quit()

