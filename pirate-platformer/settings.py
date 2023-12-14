import pygame
import os
from pygame.image import load as load_image

# FPS
FPS = 60
# game over
game_over = 0
# main menu
main_menu = True
level_menu = False
# level
level = 1
max_levels = 3
# score
score = 0
# tile size
TILE_SIZE = 50
# cols
COLS = 20
# screen size
SCREEN_WIDTH = TILE_SIZE * COLS
SCREEN_HEIGHT = TILE_SIZE * COLS 
# colors
WHITE = (255, 255, 255)
SKYBLUE = 133, 183, 199

# Actual directory
abs_dir = os.path.abspath(os.getcwd())

# Base directory
img_dir = os.path.join(abs_dir, "assets", "img")
buttons_dir = os.path.join(abs_dir, "assets", "img", "buttons")
font_dir = os.path.join(abs_dir, "assets", "fonts")
keys_dir = os.path.join(abs_dir, "assets", "img", "keys")


pygame.mixer.init()

# font
pygame.font.init()
font_score = pygame.font.SysFont('Arial', 30)
game_over_font = pygame.font.SysFont('Arial', 65)
# load external font
try :
    info_font = pygame.font.Font(os.path.join(font_dir, "pixel_font.ttf"), 50)
    info_font_2 = pygame.font.Font(os.path.join(font_dir, "pixel_font.ttf"), 30)
except FileNotFoundError as file_error:
    print("Archivo no encontrado: ", file_error)
    pygame.quit()
except pygame.error as pygame_error:
    print("Error de pygame: ", pygame_error)
    pygame.quit()
except Exception as error:
    print("Error : ", error)
    pygame.quit()

# load images
try:
    bkg_image = load_image(os.path.join(img_dir, 'background', 'background.png'))
    restart_btn = load_image(os.path.join(buttons_dir, 'restart_btn.png'))
    next_btn = load_image(os.path.join(buttons_dir, 'next_btn.png'))
    home_btn = load_image(os.path.join(buttons_dir, 'home_btn.png'))
    start_btn = load_image(os.path.join(buttons_dir, 'start_btn.png'))
    options_btn = load_image(os.path.join(buttons_dir, 'options_btn.png'))
    exit_btn = load_image(os.path.join(buttons_dir, 'exit_btn.png'))
    information_btn = load_image(os.path.join(buttons_dir, 'information_btn.png'))
    sound_btn = load_image(os.path.join(buttons_dir, 'sound_btn.png'))
    back_btn = load_image(os.path.join(buttons_dir, 'back_btn.png'))
    level_1_btn = load_image(os.path.join(buttons_dir, 'level_1_btn.png'))
    level_2_btn = load_image(os.path.join(buttons_dir, 'level_2_btn.png'))
    level_3_btn = load_image(os.path.join(buttons_dir, 'level_3_btn.png'))
    UP_arrow = load_image(os.path.join(keys_dir, 'up_arrow.png'))
    DOWN_arrow = load_image(os.path.join(keys_dir, 'down_arrow.png'))
    LEFT_arrow = load_image(os.path.join(keys_dir, 'left_arrow.png'))
    RIGHT_arrow = load_image(os.path.join(keys_dir, 'right_arrow.png'))
    SPACE_key = load_image(os.path.join(keys_dir,'SPACE_key.png'))
    W_key = load_image(os.path.join(keys_dir, 'key_W.png'))
    A_key = load_image(os.path.join(keys_dir, 'key_A.png'))
    S_key = load_image(os.path.join(keys_dir, 'key_S.png'))
    D_key = load_image(os.path.join(keys_dir, 'key_D.png'))
    F_key = load_image(os.path.join(keys_dir, 'key_F.png'))
    P_key = load_image(os.path.join(keys_dir, 'key_P.png'))
except FileNotFoundError as file_error:
    print("Archivo no encontrado: ", file_error)
    pygame.quit()
except pygame.error as pygame_error:
    print("Error de pygame: ", pygame_error)
    pygame.quit()
except Exception as error:
    print("Error : ", error)
    pygame.quit()

sounds_dir = os.path.join(abs_dir, "assets", "sounds")

try:
    pygame.mixer.music.load(os.path.join(sounds_dir, "bgm.mp3"))
    pygame.mixer.music.set_volume(0.5)
    coin_fx = pygame.mixer.Sound(os.path.join(sounds_dir, "coin.wav"))
    coin_fx.set_volume(0.5)
    jump_fx = pygame.mixer.Sound(os.path.join(sounds_dir, "jump.mp3"))
    jump_fx.set_volume(0.5)
    game_over_fx = pygame.mixer.Sound(os.path.join(sounds_dir, "game_over.mp3"))
    game_over_fx.set_volume(0.5)
    hurt_fx = pygame.mixer.Sound(os.path.join(sounds_dir, "hurt.mp3"))
    hurt_fx.set_volume(0.5)
except FileNotFoundError as file_error:
    print("Archivo no encontrado: ", file_error)
    pygame.quit()
except pygame.error as pygame_error:
    print("Error de pygame: ", pygame_error)
    pygame.quit()
except Exception as error:
    print("Error : ", error)
    pygame.quit()

# sprite groups
tile_group = pygame.sprite.Group()
pirate_enemy_group = pygame.sprite.Group()
platforms_group = pygame.sprite.Group()
traps_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()


