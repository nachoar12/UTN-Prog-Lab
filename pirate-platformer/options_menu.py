import pygame
from settings import *
from class_Button import Button
from instructions_menu import display_instructions

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

information_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2 - 150, information_btn, screen)
sound_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2, sound_btn, screen)
back_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2 + 150, back_btn, screen)

def options_menu():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(bkg_image, (0, 0))
        clock.tick(FPS)
        information_button.draw()
        sound_button.draw()
        back_button.draw() 
        if information_button.is_pressed():
            display_instructions()
        if sound_button.is_pressed():
            # mute all sounds
            pass
        if back_button.is_pressed():
            return 
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                running = False