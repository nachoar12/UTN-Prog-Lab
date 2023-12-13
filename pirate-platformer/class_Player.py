import pygame
from settings import *
from class_World import World
from functions import draw_text

class Player():
    def __init__(self, x, y, world: World, screen):
        self.reset(x, y, screen)
        self.world = world
        self.screen = screen

    def update(self, game_over):
        delta_x = 0
        delta_y = 0
        walk_cooldown = 5
        col_threshold = 20
        if game_over == 0:
            # get keypresses
            key = pygame.key.get_pressed()
            if (key[pygame.K_w] or key[pygame.K_UP]) and not self.jump and not self.in_air:
                # print('jumping')
                jump_fx.play()
                self.vel_y = -15
                self.jump = True
            if not key[pygame.K_w] and not key[pygame.K_UP]:
                self.jump = False
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                delta_x -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                delta_x += 5
                self.counter += 1
                self.direction = 1
            if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT] and not key[pygame.K_a] and not key[pygame.K_d]:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                elif self.direction == -1:
                    self.image = self.images_left[self.index]

            # handle animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                elif self.direction == -1:
                    self.image = self.images_left[self.index]

            # add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            delta_y += self.vel_y
            # check collision
            self.in_air = True
            for tile in self.world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + delta_x, self.rect.y, self.width, self.height):
                    delta_x = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + delta_y, self.width, self.height):
                    # check if below the ground / jumping
                    if self.vel_y < 0:
                        delta_y = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground / falling
                    elif self.vel_y > 0:
                        delta_y = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False


            # check for collision with enemies
            if pygame.sprite.spritecollide(self, pirate_enemy_group, False):
                self.lives -= 1
                if self.lives == 0:
                    game_over = -1
                    game_over_fx.play()
            # check for collision with spikes
            if pygame.sprite.spritecollide(self, traps_group, False):
                self.lives -= 1
                if self.lives == 0:
                    game_over = -1
                    game_over_fx.play()
            # check for collision with door
            if pygame.sprite.spritecollide(self, door_group, False):
                game_over = 1

            # check for collision with platforms
            for platform in platforms_group:
                # collision in x direction
                if platform.rect.colliderect(self.rect.x + delta_x, self.rect.y, self.width, self.height):
                    delta_x = 0
                # collision in y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + delta_y, self.width, self.height):
                    # check if below platform
                    if abs((self.rect.top + delta_y) - platform.rect.bottom) < col_threshold:
                        self.vel_y  = 0
                        delta_y = platform.rect.bottom - self.rect.top
                    # check if above platform
                    elif abs((self.rect.bottom + delta_y) - platform.rect.top) < col_threshold:
                        self.rect.bottom = platform.rect.top - 1 
                        self.in_air = False
                        delta_y = 0
                    # move with platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction


            # update player position
            self.rect.x += delta_x
            self.rect.y += delta_y
        elif game_over == -1:
            draw_text('GAME OVER', font_score, WHITE, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, self.screen)
            if self.direction == 1:
                self.image = self.dead_image
            elif self.direction == -1:
                self.image = pygame.transform.flip(
                    self.dead_image, True, False)
            if self.rect.y > 200:
                self.rect.y -= 5

        # draw player
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen, ('white'), self.rect, 2)

        return game_over

    def reset(self, x, y, screen):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(0, 4):
            img_right = pygame.image.load(f'./assets/img/pirate/{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 60))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.transform.scale(
            pygame.image.load('./assets/img/pirate/dead.png'), (35, 50))
        self.image = self.images_right[self.index]
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.lives = 3
        self.vel_y = 0
        self.jump = False
        self.direction = 0
        self.in_air = False

