import pygame
from settings import *
from class_World import World
from functions import draw_text
from class_Projectile import Projectile

class Player():
    def __init__(self, x, y, world: World, screen):
        self.reset(x, y, screen)
        self.screen = screen
        self.world = world
        self.projectile_path = './assets/img/projectile/knife.png'
        self.projectile = None
        self.projectile_group = pygame.sprite.Group()
        self.lives = 3
        global sfx_on

    def update(self, game_over, sfx):
        delta_x = 0
        delta_y = 0
        walk_cooldown = 3
        atk_cooldown = int(10 / FPS)
        col_threshold = 20
        
        if game_over == 0:
            # get keypresses
            key = pygame.key.get_pressed()
            if (key[pygame.K_w] or key[pygame.K_UP]) and not self.jump and not self.in_air:
                # print('jumping')
                if sfx:
                    jump_fx.play()
                self.vel_y = -15
                self.jump = True
            if not key[pygame.K_w] and not key[pygame.K_UP]:
                self.jump = False
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                delta_x -= 5
                self.counter += 1
                self.direction = -1
            elif key[pygame.K_RIGHT] or key[pygame.K_d]:
                delta_x += 5
                self.counter += 1
                self.direction = 1
            if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT] and not key[pygame.K_a] and not key[pygame.K_d] and not key[pygame.K_SPACE]:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                elif self.direction == -1:
                    self.image = self.images_left[self.index]
            if key[pygame.K_SPACE] == 1 and not self.attack_activated and self.projectile is None:
                self.attack_activated = True
                self.projectile = Projectile(self.rect.centerx, self.rect.centery, self.direction, self.projectile_path, 25, 15)
                self.projectile_group.add(self.projectile)
                if sfx:
                    ranged_fx.play()


            # handle movement animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                elif self.direction == -1:
                    self.image = self.images_left[self.index]

            # handle attack animation
            if self.attack_activated:
                self.attack_counter += 1

                if self.attack_counter >= atk_cooldown:
                    self.attack_counter = 0 
                    if self.direction == 1:
                        self.image = self.images_ranged_right[self.attack_index]
                    elif self.direction == -1:
                        self.image = self.images_ranged_left[self.attack_index]

                    self.attack_index += 1

                    if self.attack_index >= len(self.images_ranged_right):
                        self.attack_activated = False 
                        self.attack_index = 0  

            # add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            delta_y += self.vel_y
            # check collision with external blocks
            self.in_air = True
            # for tile in self.world.tile_list:
            #     # check for collision in x direction
            #     if tile[1].colliderect(self.rect.x + delta_x, self.rect.y, self.width, self.height):
            #         delta_x = 0
            #     # check for collision in y direction
            #     if tile[1].colliderect(self.rect.x, self.rect.y + delta_y, self.width, self.height):
            #         # check if below the ground / jumping
            #         if self.vel_y < 0:
            #             delta_y = tile[1].bottom - self.rect.top
            #             self.vel_y = 0
            #         # check if above the ground / falling
            #         elif self.vel_y > 0:
            #             delta_y = tile[1].top - self.rect.bottom
            #             self.vel_y = 0
            #             self.in_air = False

            # Check for collision with tiles 
            for tile in tile_group:
                # collision in x direction
                if tile.rect.colliderect(self.rect.x + delta_x, self.rect.y, self.width, self.height):
                    delta_x = 0
                # collision in y direction
                if tile.rect.colliderect(self.rect.x, self.rect.y + delta_y, self.width, self.height):
                    # check if below tile
                    if abs((self.rect.top + delta_y) - tile.rect.bottom) < col_threshold:
                        self.vel_y  = 0
                        delta_y = tile.rect.bottom - self.rect.top
                    # check if above tile
                    elif abs((self.rect.bottom + delta_y) - tile.rect.top) < col_threshold:
                        self.rect.bottom = tile.rect.top - 1 
                        self.in_air = False
                        delta_y = 0

            # check for collision with enemies
            if pygame.sprite.spritecollide(self, pirate_enemy_group, False):
                game_over = -1
                if sfx:
                    game_over_fx.play()
            # check for collision with spikes
            if pygame.sprite.spritecollide(self, traps_group, False):
                    game_over = -1
                    if sfx:
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
            draw_text('GAME OVER', game_over_font, WHITE, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2, self.screen)
            if self.direction == 1:
                self.image = self.dead_image
            elif self.direction == -1:
                self.image = pygame.transform.flip(
                    self.dead_image, True, False)
            if self.rect.y > 200:
                self.rect.y -= 5
        elif game_over == 1:
             draw_text('LEVEL COMPLETED', game_over_font, WHITE, SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2, self.screen)

        # check projectile collision
        # for projectile in self.projectile_group:
        #     if pygame.sprite.spritecollide(projectile, pirate_enemy_group, True): 
        #         self.projectile = None
        #         self.attack_activated = False
        #         if sfx:
        #             hit_fx.play()



        self.projectile_group.update()

        # Remove the projectile if it's off-screen
        if self.projectile and (self.projectile.rect.x < 0 - self.projectile.width or self.projectile.rect.x > SCREEN_WIDTH + self.projectile.width):
            self.projectile = None 

        # draw projectiles
        self.projectile_group.draw(self.screen)


        # draw player
        self.screen.blit(self.image, self.rect)
        #debug
        # pygame.draw.rect(self.screen, ('white'), self.rect, 2)

        return game_over

    def load_animatios(self, action:str, number_of_frames, direction:str = 'right'):
        list_of_frames = []
        for i in range(0,number_of_frames - 1):
            img = pygame.image.load(f'./assets/img/pirate/{action}_{i}.png')
            img = pygame.transform.scale(img, (TILE_SIZE // 2, TILE_SIZE))
            if direction == 'left':
                img = pygame.transform.flip(img, True, False)
            list_of_frames.append(img)
        return list_of_frames
    
    def reset(self, x, y, screen):
        self.images_right = self.load_animatios('run', 4)
        self.images_left = self.load_animatios('run', 4, 'left')
        self.images_ranged_right = self.load_animatios('ranged', 3)
        self.images_ranged_left = self.load_animatios('ranged', 3, 'left')
        self.index = 0
        self.counter = 0
        self.attack_index = 0
        self.attack_counter = 0
        self.attack_activated = False
        self.dead_image = pygame.transform.scale(
            pygame.image.load('./assets/img/pirate/dead.png'), (35, 50))
        self.image = self.images_right[self.index]
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jump = False
        self.direction = 1
        self.in_air = False
        

