import pygame
from settings import TILE_SIZE, platforms_group, pirate_enemy_group, coin_group, traps_group, door_group, tile_group, power_up_group,life_group, SCREEN_HEIGHT
from class_Enemy import Enemy
from class_Boss import Boss
from class_Trap import Trap
from class_Door import Door
from class_Coin import Coin
from class_Platform import Platform
from class_Tile import Tile
from class_PowerUp import PowerUp
from os import path
import pickle



class World():
    def __init__(self, level, screen):
        # load images
        self.tile_list = []
        self.screen = screen
        right_tile = pygame.image.load('assets\img\\tiles\\right_tile.png')
        top_right_tile = pygame.image.load(
            './assets/img/tiles/top_right_tile.png')
        top_tile = pygame.image.load('./assets/img/tiles/top_tile.png')
        top_left_tile = pygame.image.load(
            './assets/img/tiles/top_left_tile.png')
        left_tile = pygame.image.load('./assets/img/tiles/left_tile.png')
        floor_tile = pygame.image.load('./assets/img/tiles/floor_tile.png')
        life_img = pygame.image.load('./assets/img/life/life.png')
        clock_img = pygame.image.load('./assets/img/power/clock.png')
        row_count = 0
        self.level_data = level
        for row in self.level_data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    tile = Tile(col_count * TILE_SIZE, row_count * TILE_SIZE, floor_tile)
                    tile_group.add(tile)
                elif tile == 2:
                    tile = Tile(col_count * TILE_SIZE, row_count * TILE_SIZE, right_tile)
                    tile_group.add(tile)
                elif tile == 3:
                    tile = Tile(col_count * TILE_SIZE, row_count * TILE_SIZE, top_right_tile)
                    tile_group.add(tile)
                elif tile == 4:
                    tile = Tile(col_count * TILE_SIZE, row_count * TILE_SIZE, top_tile)
                    tile_group.add(tile)
                elif tile == 5:
                    tile = Tile(col_count * TILE_SIZE, row_count * TILE_SIZE, left_tile)
                    tile_group.add(tile)
                elif tile == 6:
                    tile = Tile(col_count * TILE_SIZE, row_count * TILE_SIZE, top_left_tile)
                    tile_group.add(tile)
                elif tile == 7:
                    pirate_enemy = Enemy(
                        col_count * TILE_SIZE, row_count * TILE_SIZE + TILE_SIZE // 4 - 10, screen)
                    pirate_enemy_group.add(pirate_enemy)
                elif tile == 8:
                    traps = Trap(col_count * TILE_SIZE,
                                 row_count * TILE_SIZE + TILE_SIZE // 1.5)
                    traps_group.add(traps)
                elif tile == 9:
                    coin = Coin(col_count * TILE_SIZE + TILE_SIZE // 4, row_count * TILE_SIZE)
                    coin_group.add(coin)
                elif tile == 10:
                    # horizontal platform
                    platform = Platform(
                        col_count * TILE_SIZE, row_count * TILE_SIZE + TILE_SIZE // 2, 1, 0, screen)
                    platforms_group.add(platform)
                elif tile == 11:
                    door = Door(col_count * TILE_SIZE - TILE_SIZE // 3,
                                row_count * TILE_SIZE // 2)
                    door_group.add(door)
                elif tile == 12:
                    # vertical platform
                    platform = Platform(
                        col_count * TILE_SIZE, row_count * TILE_SIZE + TILE_SIZE // 2, 0, 1, screen)
                    platforms_group.add(platform)
                elif tile == 13:
                    boss = Boss(col_count * TILE_SIZE, row_count * TILE_SIZE, screen)
                    pirate_enemy_group.add(boss)
                elif tile == 14:
                    life = PowerUp(col_count * TILE_SIZE, row_count * TILE_SIZE, life_img)
                    life_group.add(life)
                elif tile == 15:
                    power_up = PowerUp(col_count * TILE_SIZE, row_count * TILE_SIZE, clock_img)
                    power_up_group.add(power_up)
                col_count += 1
            row_count += 1

    def set_level(self, level_number):
        # load in level data and create world
        if path.exists(f'level{level_number}_data'):
            pickle_in = open(f'level{level_number}_data', 'rb')
            self.level_data = pickle.load(pickle_in)
        return self.level_data

    def draw(self):
        ...
        # for tile in self.tile_list:
        #     self.screen.blit(tile[0], tile[1])
        # debug 
        # for tile in tile_group:
        #     pygame.draw.rect(self.screen, ('white'), tile.rect, 2)
        # for coin in coin_group:
        #     pygame.draw.rect(self.screen, ('yellow'), coin.rect, 2)
        # for door in door_group:
        #     pygame.draw.rect(self.screen, ('red'), door.rect, 2)
        # for trap in traps_group:
        #     pygame.draw.rect(self.screen, ('blue'), trap.rect, 2)
        # for platform in platforms_group:
        #     pygame.draw.rect(self.screen, ('white'), platform.rect, 2)