from typing import Any
import pygame
from pygame.locals import *
from settings import *
import pickle
from os import path
from functions import draw_text
from class_World import World
from class_Button import Button
from class_Enemy import Enemy
from class_Trap import Trap
from class_Door import Door
from class_Coin import Coin
from class_Player import Player
from class_Platform import Platform



pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pirate Plarforms')
clock = pygame.time.Clock()
screen.fill(SKYBLUE)

# function to reset level

def reset_level(level):
    player.reset(100, SCREEN_HEIGHT - 110, screen)
    pirate_enemy_group.empty()
    traps_group.empty()
    door_group.empty()
    platforms_group.empty()
    # load in level data and create world
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data, screen)
    
    return world


# load in level data and create world
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
world = World(world_data, screen)
player = Player(100, SCREEN_HEIGHT - 110, world, screen)
score_coin = Coin(0, 0)
coin_group.add(score_coin)

# create buttons
restart_button = Button(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 100, restart_btn, screen)
home_button = Button(SCREEN_WIDTH // 2 - 65, SCREEN_HEIGHT // 2 + 100, home_btn, screen)

start_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2 - 100, start_btn, screen)
options_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2, options_btn, screen)
exit_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5, SCREEN_HEIGHT // 2 + 100, exit_btn, screen)

level_1_button = Button(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2, level_1_btn,screen)
level_2_button = Button(SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2, level_2_btn, screen)
level_3_button = Button(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 2, level_2_btn, screen)


music_playing = True
pygame.mixer.music.play(-1, 0.0, 5000)
run = True
while run:
    clock.tick(FPS)

    screen.blit(bkg_image, (0, 0))
    if main_menu:
        if exit_button.draw():
            run = False
        if options_button.draw():
            # options menu
            pass
        if start_button.draw():
            main_menu = False
            # level selector 

        
    else:
        world.draw()

        if game_over == 0:
            pirate_enemy_group.update()
            platforms_group.update()
            # update score
            # check collision with coins
            if pygame.sprite.spritecollide(player, coin_group, True):
                coin_fx.play()
                score += 1
            draw_text('X ' + str(score), font_score, WHITE, TILE_SIZE - 10, 10, screen)

        pirate_enemy_group.draw(screen)
        platforms_group.draw(screen)
        traps_group.draw(screen)
        coin_group.draw(screen)
        door_group.draw(screen)

        game_over = player.update(game_over)

        # if player has died
        if game_over == -1:
            if restart_button.draw():
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0
            # elif home_button.draw():
            #     run = False
        # if player completed the level
        if game_over == 1:
            # reset game and next level
            level += 1
            if level <= max_levels:
                # reset level
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                if restart_button.draw():
                    level = 1
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # print(score)
    pygame.display.update()

pygame.quit()
