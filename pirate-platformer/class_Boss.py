import pygame
from settings import TILE_SIZE, SCREEN_WIDTH, projectile_fx, sfx_on
from class_Projectile import Projectile
from random import randint


class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.animation_speed = 10  # Adjust as needed for animation speed
        self.index = 0
        self.images = self.load_animations('spell', 8)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.move_direction = 1
        self.move_counter = 0
        self.screen = screen
        self.projectile_group = pygame.sprite.Group()
        self.projectile_path = './assets/img/projectile/round_shot.png'
        self.projectile_cooldown = 120
        self.projectile_timer = 0
        self.lives = 5
        global sfx_on

    def load_animations(self, action: str, number_of_frames, direction: str = 'right'):
        list_of_frames = []
        for i in range(0, number_of_frames - 1):
            img = pygame.image.load(f'./assets/img/enemy/{action}_{i}.png')
            img = pygame.transform.scale(img, (TILE_SIZE * 1.3, TILE_SIZE))
            if direction == 'left':
                img = pygame.transform.flip(img, True, False)
            list_of_frames.append(img)
        return list_of_frames

    def update(self, game_over,sfx):
        # Movement and animation logic
        self.index += 1
        if self.index >= len(self.images) * self.animation_speed:
            self.index = 0

        self.image = self.images[self.index // self.animation_speed]
        # debug
        # pygame.draw.rect(self.screen, ('green'), self.rect, 2)

        self.projectile_timer += 1
        if self.projectile_timer >= self.projectile_cooldown:
            self.projectile_timer = 0
            for i in range(3):
                random_pos = randint(6,16) * TILE_SIZE
                boss_projectile = Projectile(0, random_pos, self.move_direction, self.projectile_path, TILE_SIZE // 3.5, TILE_SIZE // 3.5, 4)
                self.projectile_group.add(boss_projectile)
            if sfx:
                projectile_fx.play()
        if self.lives <= 0:
            game_over = 1
            if sfx:
                print('victory')
                # victory_sound.play()
        # Update enemy projectiles
        self.projectile_group.update()

        # remove off-screen projectiles
        # for projectile in self.projectile_group:
        #     if projectile.rect.x < 0 - projectile.width or projectile.rect.x > SCREEN_WIDTH + projectile.width:
        #         projectile.kill()

        # Draw enemy projectiles
        self.projectile_group.draw(self.screen)

        return game_over
