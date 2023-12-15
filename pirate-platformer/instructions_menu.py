import pygame
from settings import *
from class_Button import Button
from class_Key import Key
from functions import draw_text

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

back_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5,
                     SCREEN_HEIGHT // 2 + 400, back_btn, screen)
up_arrow = Key(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT //
               2 - TILE_SIZE * 1.5, UP_arrow, screen)
down_arrow = Key(SCREEN_WIDTH // 2 - 250,
                 SCREEN_HEIGHT // 2, DOWN_arrow, screen)
left_arrow = Key(SCREEN_WIDTH // 2 - 350,
                 SCREEN_HEIGHT // 2, LEFT_arrow, screen)
right_arrow = Key(SCREEN_WIDTH // 2 - 150,
                  SCREEN_HEIGHT // 2, RIGHT_arrow, screen)
w_key = Key(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT //
            2 - TILE_SIZE * 1.5, W_key, screen)
s_key = Key(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 2, S_key, screen)
a_key = Key(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2, A_key, screen)
d_key = Key(SCREEN_WIDTH // 2 + 300, SCREEN_HEIGHT // 2, D_key, screen)
p_key = Key(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 + 275, P_key, screen)
space_key = Key(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT //
                2 + 275, SPACE_key, screen)


def display_instructions():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(bkg_image, (0, 0))
        clock.tick(FPS)
        draw_text('Game Controls', info_font, WHITE, SCREEN_WIDTH //
                  2 - 300, SCREEN_HEIGHT // 2 - 400, screen)
        back_button.draw()
        draw_text('Movement Keys', info_font, WHITE, SCREEN_WIDTH //
                  2 - 300, SCREEN_HEIGHT // 2 - 225, screen)
        up_arrow.draw()
        down_arrow.draw()
        left_arrow.draw()
        right_arrow.draw()
        w_key.draw()
        s_key.draw()
        a_key.draw()
        d_key.draw()
        draw_text('Action Keys', info_font, WHITE, SCREEN_WIDTH //
                  2 - 300, SCREEN_HEIGHT // 2 + 125, screen)
        draw_text('Range Attack', info_font_2, WHITE, SCREEN_WIDTH //
                  2 + 75, SCREEN_HEIGHT // 2 + 200, screen)
        draw_text('Pause', info_font_2, WHITE, SCREEN_WIDTH //
                  2 - 350, SCREEN_HEIGHT // 2 + 200, screen)
        p_key.draw()
        space_key.draw()

        if back_button.is_pressed():
            return
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                running = False


# display_instructions()
