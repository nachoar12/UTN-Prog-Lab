from typing import Any
import pygame
from pygame.locals import *
from settings import *
import pickle
from os import path
from functions import draw_text
from class_World import World
from class_Button import Button
from class_Player import Player
from start_menu import start_menu

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pirate Plarforms')
clock = pygame.time.Clock()


# function to reset level

def reset_level(level):
    global world
    player.reset(100, SCREEN_HEIGHT - 110, screen)
    tile_group.empty()
    pirate_enemy_group.empty()
    traps_group.empty()
    door_group.empty()
    platforms_group.empty()
    coin_group.empty()
    # load in level data and create world
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data, screen)

    return world


def set_level(level):
    # load in level data and create world
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)

    return world_data


# create buttons
restart_button = Button(SCREEN_WIDTH // 2 - 80,
                        SCREEN_HEIGHT // 2 - 150, restart_btn, screen)
next_button = Button(SCREEN_WIDTH // 2 - 80,
                     SCREEN_HEIGHT // 2 + 150, next_btn, screen)
home_button = Button(SCREEN_WIDTH // 2 - 65,
                     SCREEN_HEIGHT // 2 + 100, home_btn, screen)

start_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5,
                      SCREEN_HEIGHT // 2 - 100, start_btn, screen)
options_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE *
                        1.5, SCREEN_HEIGHT // 2, options_btn, screen)
exit_button = Button(SCREEN_WIDTH // 2 - TILE_SIZE * 1.5,
                     SCREEN_HEIGHT // 2 + 100, exit_btn, screen)

level_1_button = Button(SCREEN_WIDTH // 2 - 400,
                        SCREEN_HEIGHT // 2, level_1_btn, screen)
level_2_button = Button(SCREEN_WIDTH // 2 - 100,
                        SCREEN_HEIGHT // 2, level_2_btn, screen)
level_3_button = Button(SCREEN_WIDTH // 2 + 200,
                        SCREEN_HEIGHT // 2, level_3_btn, screen)

music_playing = True
pygame.mixer.music.play(-1, 0.0, 5000)
run = True
level_selected = start_menu()
# level_selected = 5
world = World(set_level(level_selected), screen)

player = Player(100, SCREEN_HEIGHT - 110, world, screen)
while run:
    clock.tick(FPS)
    screen.blit(bkg_image, (0, 0))
    world.draw()

    if game_over == 0:
        tile_group.update()
        pirate_enemy_group.update()
        platforms_group.update()
        # update score
        # check collision with coins
        if pygame.sprite.spritecollide(player, coin_group, True):
            coin_fx.play()
            score += 1
        draw_text('Coins ' + str(score), font_score, WHITE, 5, 10, screen)
    tile_group.draw(screen)
    pirate_enemy_group.draw(screen)
    platforms_group.draw(screen)
    traps_group.draw(screen)
    coin_group.draw(screen)
    door_group.draw(screen)

    game_over = player.update(game_over)

    # if player has died
    if game_over == -1:
        restart_button.draw()
        if restart_button.is_pressed():
            world_data = []
            world = reset_level(level_selected)
            game_over = 0
            score = 0
    # if player completed the level
    if game_over == 1:
        restart_button.draw()
        next_button.draw()
        if restart_button.is_pressed():
            world_data = []
            world = reset_level(level_selected)
            game_over = 0
        elif next_button.is_pressed():
            # reset game and next level
            level_selected += 1
            if level <= max_levels:
                # reset level
                world_data = []
                world = reset_level(level_selected)
                game_over = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
