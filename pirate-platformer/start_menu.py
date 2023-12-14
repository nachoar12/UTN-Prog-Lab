import pygame
from settings import *
from class_Button import Button
from level_selector import level_selector
from options_menu import options_menu

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

start_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2 - 200, start_btn, screen)
options_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2, options_btn, screen)
exit_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2 + 200, exit_btn, screen)


def start_menu():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(bkg_image, (0, 0))
        clock.tick(FPS)
        exit_button.draw()
        options_button.draw()
        start_button.draw() 
        if exit_button.is_pressed():
            running = False
        if options_button.is_pressed():
            options_menu()
            pass
        if start_button.is_pressed():
            level = level_selector()
            return level
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                running = False

# start_menu()


