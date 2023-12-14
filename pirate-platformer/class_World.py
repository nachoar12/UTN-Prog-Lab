import pygame
from settings import TILE_SIZE, platforms_group, pirate_enemy_group, coin_group, traps_group, door_group, tile_group, SCREEN_HEIGHT
from class_Enemy import Enemy
from class_Trap import Trap
from class_Door import Door
from class_Coin import Coin
from class_Platform import Platform
from class_Floor import Floor
from os import path
import pickle


class World():
    def __init__(self, level, screen):
        # load images
        self.tile_list = []
        self.screen = screen
        right_tile = pygame.image.load('./assets/img/tiles/right_tile.png')
        top_right_tile = pygame.image.load(
            './assets/img/tiles/top_right_tile.png')
        top_tile = pygame.image.load('./assets/img/tiles/top_tile.png')
        top_left_tile = pygame.image.load(
            './assets/img/tiles/top_left_tile.png')
        left_tile = pygame.image.load('./assets/img/tiles/left_tile.png')
        floor_tile = pygame.image.load('./assets/img/tiles/floor_tile.png')
        row_count = 0
        self.level_data = level
        for row in self.level_data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    tile = Floor(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    tile_group.add(tile)
                elif tile == 2:
                    img = pygame.transform.scale(
                        right_tile, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 3:
                    img = pygame.transform.scale(
                        top_right_tile, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 4:
                    img = pygame.transform.scale(
                        top_tile, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 5:
                    img = pygame.transform.scale(
                        left_tile, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 6:
                    img = pygame.transform.scale(
                        top_left_tile, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 7:
                    pirate_enemy = Enemy(
                        col_count * TILE_SIZE, row_count * TILE_SIZE + TILE_SIZE // 4, screen)
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

                col_count += 1
            row_count += 1

    def set_level(self, level_number):
        # load in level data and create world
        if path.exists(f'level{level_number}_data'):
            pickle_in = open(f'level{level_number}_data', 'rb')
            self.level_data = pickle.load(pickle_in)
        return self.level_data

    def draw(self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
        # debug 
        for tile in tile_group:
            pygame.draw.rect(self.screen, ('white'), tile.rect, 2)
        for coin in coin_group:
            pygame.draw.rect(self.screen, ('yellow'), coin.rect, 2)
        for door in door_group:
            pygame.draw.rect(self.screen, ('red'), door.rect, 2)
        for trap in traps_group:
            pygame.draw.rect(self.screen, ('blue'), trap.rect, 2)
        for platform in platforms_group:
            pygame.draw.rect(self.screen, ('white'), platform.rect, 2)