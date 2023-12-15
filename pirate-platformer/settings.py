import pygame
import os
from functions import load_images_from_json, load_sounds_from_json
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
# sounds
music_on = True
sfx_on = True
# pause
is_paused = False
abs_dir = os.path.abspath(os.getcwd())
imgs_dir = os.path.join(abs_dir, 'image_paths.json')
sounds_dir = os.path.join(abs_dir, 'sound_paths.json')
font_dir = os.path.join(abs_dir, 'assets', 'fonts')

# import images
img_data = load_images_from_json(imgs_dir)
sound_data = load_sounds_from_json(sounds_dir)

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

bkg_image = img_data['background_image']
restart_btn = img_data['restart_button']
next_btn = img_data['next_button']
home_btn = img_data['home_button']
start_btn = img_data['start_button']
options_btn = img_data['options_button']
exit_btn = img_data['exit_button']
information_btn = img_data['information_button']
sound_btn = img_data['sound_button']
music_btn = img_data['music_button']
back_btn = img_data['back_button']
level_1_btn = img_data['level_1_button']
level_2_btn = img_data['level_2_button']
level_3_btn = img_data['level_3_button']
UP_arrow = img_data['up_arrow']
DOWN_arrow = img_data['down_arrow']
LEFT_arrow = img_data['left_arrow']
RIGHT_arrow = img_data['right_arrow']
SPACE_key = img_data['space_key']
W_key = img_data['key_W']
A_key = img_data['key_A']
S_key = img_data['key_S']
D_key = img_data['key_D']
F_key = img_data['key_F']
P_key = img_data['key_P']

# load sounds

pygame.mixer.init()

bgm_music = pygame.mixer.music.load("assets/sounds/bgm.mp3")
pygame.mixer.music.set_volume(0.5)
coin_fx = sound_data['coin_sound']
coin_fx.set_volume(0.5)
jump_fx = sound_data['jump_sound']
jump_fx.set_volume(0.5)
game_over_fx = sound_data['game_over_sound']
game_over_fx.set_volume(0.5)
hurt_fx = sound_data['hurt_sound']
hurt_fx.set_volume(0.5)
ranged_fx = sound_data['ranged_sound']
ranged_fx.set_volume(0.5)
hit_fx = sound_data['hit_sound']
hit_fx.set_volume(0.5)
projectile_fx = sound_data['projectile_sound']
projectile_fx.set_volume(0.3)
power_fx = sound_data['power_sound']
power_fx.set_volume(0.5)


# sprite groups
tile_group = pygame.sprite.Group()
pirate_enemy_group = pygame.sprite.Group()
platforms_group = pygame.sprite.Group()
traps_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
life_group = pygame.sprite.Group()
power_up_group = pygame.sprite.Group()


