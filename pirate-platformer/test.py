import pygame
from settings import *
from class_Button import Button
from instructions_menu import display_instructions
from functions import draw_text

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

information_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 6,
                            SCREEN_HEIGHT // 2 - TILE_SIZE * 3, information_btn, screen)
sound_button = Button(SCREEN_WIDTH // 2 + TILE_SIZE * 3,
                      SCREEN_HEIGHT // 2 - TILE_SIZE * 3, sound_btn, screen)
back_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5,
                     SCREEN_HEIGHT // 2 + TILE_SIZE * 3, back_btn, screen)

def options_menu():
    clock = pygame.time.Clock()
    running = True
    global sound_on, sfx_on

    while running:
        screen.blit(bkg_image, (0, 0))
        clock.tick(FPS)
        information_button.draw()
        sound_button.draw()
        sfx_button.draw()
        back_button.draw()

        # Display whether sound and SFX are on or off
        if sound_on:
            draw_text("Sound: ON", info_font_2, WHITE, SCREEN_WIDTH // 2 + TILE_SIZE * 4, SCREEN_HEIGHT // 2 - TILE_SIZE * 3, screen)
        else:
            draw_text("Sound: OFF", info_font_2, WHITE, SCREEN_WIDTH // 2 + TILE_SIZE * 4, SCREEN_HEIGHT // 2 - TILE_SIZE * 3, screen)

        if sfx_on:
            draw_text("SFX: ON", info_font_2, WHITE, SCREEN_WIDTH // 2 + TILE_SIZE * 4, SCREEN_HEIGHT // 2, screen)
        else:
            draw_text("SFX: OFF", info_font_2, WHITE, SCREEN_WIDTH // 2 + TILE_SIZE * 4, SCREEN_HEIGHT // 2, screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False  # Return False to resume the game

        # Check for button presses
        if back_button.is_pressed():
            return True  # Return True to resume the game
        elif sound_button.is_pressed():
            sound_on = not sound_on
            # Handle sound toggling (mute/unmute sound)
            if sound_on:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
        elif sfx_button.is_pressed():
            sfx_on = not sfx_on
            # Handle SFX toggling (mute/unmute SFX)
            # Code to mute/unmute your sound effects (projectiles, jump, collision, etc.)

    return False  # Return False if the 'Back' button was not pressed (to exit the game or continue game logic)

options_menu()