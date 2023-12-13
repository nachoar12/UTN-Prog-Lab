import pygame
from settings import TILE_SIZE, platforms_group, pirate_enemy_group, coin_group, traps_group, door_group
from class_Enemy import Enemy
from class_Trap import Trap
from class_Door import Door
from class_Coin import Coin
from class_Platform import Platform

class World():
    def __init__(self, level: list, screen):
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
        for row in level:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(
                        floor_tile, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
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
                    traps = Trap(col_count * TILE_SIZE, row_count * TILE_SIZE + TILE_SIZE // 2)
                    traps_group.add(traps)
                elif tile == 9:
                    coin = Coin(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    coin_group.add(coin)
                elif tile == 10:
                    # horizontal platform
                    platform = Platform(col_count * TILE_SIZE, row_count * TILE_SIZE + TILE_SIZE // 2, 1, 0, screen)
                    platforms_group.add(platform)
                elif tile == 11:
                    door = Door(col_count * TILE_SIZE - 37,  row_count * TILE_SIZE - 50 )
                    door_group.add(door)
                elif tile == 12:
                    # vertical platform
                    platform = Platform(col_count * TILE_SIZE, row_count * TILE_SIZE + TILE_SIZE // 2, 0, 1, screen)
                    platforms_group.add(platform)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
            # pygame.draw.rect(self.screen, ('red'), tile[1], 2)