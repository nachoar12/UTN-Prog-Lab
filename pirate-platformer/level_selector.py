import pygame
from settings import *
from class_Button import Button

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

level_1_button = Button(SCREEN_WIDTH // 2 - 350, SCREEN_HEIGHT // 2, level_1_btn, screen)
level_2_button = Button(SCREEN_WIDTH // 2 - 70,SCREEN_HEIGHT // 2, level_2_btn, screen)
level_3_button = Button(SCREEN_WIDTH // 2 + 200,SCREEN_HEIGHT // 2, level_3_btn, screen)


def level_selector():
    clock = pygame.time.Clock()
    running = True
    contador_de_clicks = 0

    while running:
        screen.blit(bkg_image, (0, 0))
        clock.tick(FPS)
        level_1_button.draw()
        level_2_button.draw()
        level_3_button.draw()
        if level_1_button.is_pressed():
            level = 1
            # print("level 1")
            return level
        if level_2_button.is_pressed():
            level = 2
            # print("level 2")
            return level
        if level_3_button.is_pressed():
            level = 3
            # print("level 3")
            return level
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                running = False

        pygame.display.update()

# level_selector()
    
    
