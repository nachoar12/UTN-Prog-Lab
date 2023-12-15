from typing import Any
import pygame
from pygame.locals import *
from settings import *
import pickle
from os import path
from functions import draw_text, save_player_data, get_best_results
from class_World import World
from class_Button import Button
from class_Player import Player
from class_PowerUp import PowerUp
from start_menu import start_menu
from options_menu import options_menu
import sqlite3

# Conexión a la base de datos (si no existe, se creará)
conn = sqlite3.connect('game_register.db')
cursor = conn.cursor()

# Creación de la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL,
        max_level INTEGER NOT NULL
    )
''')

name = input("Ingrese su nombre: ")


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pirate Plarforms')
clock = pygame.time.Clock()

life_img = pygame.image.load('./assets/img/life/life.png')
clock_img = pygame.image.load('./assets/img/power/clock.png')

power_up = PowerUp(9 * TILE_SIZE, 6 * TILE_SIZE, clock_img)
life = PowerUp(19 * TILE_SIZE, 6 * TILE_SIZE, life_img)

# function to reset level

def reset_level(level, x=100, y=SCREEN_HEIGHT - 110):
    # global world
    player.reset(x, y, screen)
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

pygame.mixer.music.play(-1, 0.0, 5000)
level_selected = start_menu()
# level_selected = 5
world = World(set_level(level_selected), screen)
if level_selected == 3:
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 110, world, screen)
else:
    player = Player(100, SCREEN_HEIGHT - 110, world, screen)
run = True
show_options_menu = False
game_over_save = False
win_save = False
time = 60
gameTime = pygame.time.get_ticks()
while run:
    clock.tick(FPS)
    currentTime = pygame.time.get_ticks()
    screen.blit(bkg_image, (0, 0))
    level_selected
    if currentTime - gameTime > 1000:
        time -= 1
        gameTime = currentTime
    if game_over == 0 and not is_paused:
        # tile_group.update()
        pirate_enemy_group.update(game_over, sfx_on)
        platforms_group.update()
        power_up_group.update()
        life_group.update()
        # update score
        # check collision with coins
        if pygame.sprite.spritecollide(player, coin_group, True):
            score += 1
            if sfx_on:
                coin_fx.play()

        # check collision with enemy projectiles
        for enemy in pirate_enemy_group:
            print(enemy.projectile_group)
            for enemy_projectile in enemy.projectile_group:
                if pygame.sprite.collide_rect(player, enemy_projectile):
                    enemy_projectile.kill()
                    player.lives -= 1
                    if sfx_on:
                        hurt_fx.play()
                    if player.lives <= 0:  # Check if player has no more lives
                        game_over = -1
                        if sfx_on:
                            game_over_fx.play()
        # check collision between enemies and player projectiles
            for enemy in pirate_enemy_group:
                if pygame.sprite.spritecollide(enemy, player.projectile_group, True):
                    player.projectile = None
                    player.attack_activated = False
                    score += 10
                    if sfx_on:
                        hit_fx.play()
                    if level_selected == 3:
                        enemy.lives -= 1
                        power_up_group.add(power_up)
                        life_group.add(life)
                    else:
                        enemy.kill()
        # check collision for  power up
            for power_up in power_up_group:
                if player.rect.colliderect(power_up.rect):
                    time += 60
                    if sfx_on:
                        power_fx.play()
                    power_up.kill()
        # check collision for life
            for life in life_group:
                if player.rect.colliderect(life.rect):
                    player.lives += 1
                    if sfx_on:
                        power_fx.play()
                    life.kill()

        if player.lives > 3:
            player.lives = 3
            
        tile_group.draw(screen)
        pirate_enemy_group.draw(screen)
        platforms_group.draw(screen)
        traps_group.draw(screen)
        coin_group.draw(screen)
        door_group.draw(screen)
        power_up_group.draw(screen)
        life_group.draw(screen)
    draw_text('Coins ' + str(score), font_score, WHITE, 5, 10, screen)
    for live in range(player.lives):
        draw_text('Lives:', font_score, WHITE, SCREEN_WIDTH - 190, 8, screen)
        if player.lives == 3:
            draw_text('O O O', font_score, WHITE, SCREEN_WIDTH - 100, 10, screen)
        elif player.lives == 2:
            draw_text('O O', font_score, WHITE, SCREEN_WIDTH - 100, 10, screen)
        elif player.lives == 1:
            draw_text('O', font_score, WHITE, SCREEN_WIDTH - 100, 10, screen)

    if level_selected == 3:
        for enemy in pirate_enemy_group:
            draw_text('Boss Lives: ' + str(enemy.lives), font_score, WHITE, SCREEN_WIDTH // 2 - 100, 10, screen)
            draw_text('Time: ' + str(time), font_score, WHITE, SCREEN_WIDTH // 2 - 300, 10, screen)
            game_over = enemy.update(game_over, sfx_on)
    else:
        draw_text('Time: ' + str(time), font_score, WHITE, SCREEN_WIDTH // 2 - 50, 10, screen)

    game_over = player.update(game_over, sfx_on)
    # time condition
    if time <= 0:
        game_over = -1
    # if player has died or time is 0
    if game_over == -1:
        if not game_over_save: 
            save_player_data(name, score, level_selected) 
        time = 0
   
        restart_button.draw()
        if restart_button.is_pressed():
            world_data = []
            if level_selected == 3:
                world = reset_level(level_selected, SCREEN_WIDTH //2)
            else:
                world = reset_level(level_selected)
            game_over = 0
            score = 0
            time = 60
            player.lives = 3
            game_over_save = False
    # if player completed the level
    if game_over == 1:
        if not win_save:
            save_player_data(name, score, level_selected)
            win_save = True
        
        restart_button.draw()
        next_button.draw()
        if restart_button.is_pressed():
            # reset the level
            world_data = []
            if level_selected == 3:
                if level_selected == 3:
                    world = reset_level(level_selected, SCREEN_WIDTH //2)
                else:
                    world = reset_level(level_selected)
            game_over = 0
            win_save = False
        elif next_button.is_pressed():
            # next level
            level_selected += 1
            if level <= max_levels:
                # reset level
                world_data = []
                if level_selected == 3:
                    world = reset_level(level_selected, SCREEN_WIDTH //2)
                else:
                    world = reset_level(level_selected)
                game_over = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    is_paused = not is_paused
                    if is_paused:
                        r,sfx_on = options_menu()
                        is_paused = False 
                        pygame.time.delay(100)
                    # print(r,l)
    print(game_over_save, win_save)
    pygame.display.update()
conn.close()
pygame.quit()
best_results = get_best_results(5)
print("Best Results:", best_results)
