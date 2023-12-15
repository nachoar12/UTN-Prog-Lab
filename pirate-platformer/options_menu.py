import pygame
from settings import *
from class_Button import Button
from instructions_menu import display_instructions
from functions import draw_text

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

information_button = Button(SCREEN_WIDTH // 2 + TILE_SIZE * 3,
                            SCREEN_HEIGHT // 2 - TILE_SIZE * 3, information_btn, screen)
sound_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 6,
                      SCREEN_HEIGHT // 2 + TILE_SIZE * 3, sound_btn, screen)
music_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 6,
                     SCREEN_HEIGHT // 2 - TILE_SIZE * 3, music_btn, screen)
back_button = Button(SCREEN_WIDTH // 2 + TILE_SIZE * 3,
                     SCREEN_HEIGHT // 2 + TILE_SIZE * 3, back_btn, screen)


def toggle_sfx(sfx_on):
    sfx_on = not sfx_on
    return sfx_on

def options_menu():
    clock = pygame.time.Clock()
    running = True
    global sfx_on, music_on
    # global is_paused

    while running:
        screen.blit(bkg_image, (0, 0))
        clock.tick(FPS)
        information_button.draw()
        sound_button.draw()
        music_button.draw()
        back_button.draw()

            
        if music_on:
            draw_text(":ON", info_font_2, 'green', SCREEN_WIDTH // 2 -
                      TILE_SIZE * 2.5, SCREEN_HEIGHT // 2 - TILE_SIZE * 2.9, screen)
        else:
            draw_text(":OFF", info_font_2, 'red', SCREEN_WIDTH // 2 -
                      TILE_SIZE * 2.5, SCREEN_HEIGHT // 2 - TILE_SIZE * 2.9, screen)
        if sfx_on:
            draw_text(":ON", info_font_2, 'green', SCREEN_WIDTH // 2 -
                      TILE_SIZE * 2.5, SCREEN_HEIGHT // 2 + TILE_SIZE * 3.1, screen)
        else:
            draw_text(":OFF", info_font_2, 'red', SCREEN_WIDTH // 2 -
                      TILE_SIZE * 2.5, SCREEN_HEIGHT // 2 + TILE_SIZE * 3.1, screen)

        if information_button.is_pressed():
            display_instructions()
        if music_button.is_pressed():
            music_on = not music_on
            if music_on:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
            # print(music_on)
        if sound_button.is_pressed():
            sfx_on = toggle_sfx(sfx_on) 
            # print(sfx_on)
        if back_button.is_pressed():
            return (True, sfx_on)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    return (True, sfx_on)
                
        if back_button.is_pressed():
            return (True, sfx_on) 
        
    return (True, sfx_on)


# options_menu()
# retur = options_menu()
# print(retur)