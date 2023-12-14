import pygame
from settings import TILE_SIZE

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('./assets/img/enemy/pirate_enemy.png')
        self.right_img = pygame.transform.scale(img, (TILE_SIZE // 2, TILE_SIZE // 1.3))
        self.left_img = pygame.transform.flip(self.right_img, True, False)
        self.image = self.right_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        self.screen = screen

    def update(self):
        if self.move_direction < 0 :
            self.image = self.left_img
        elif self.move_direction > 0 :
            self.image = self.right_img
        # debug
        # pygame.draw.rect(self.screen, ('red'), self.rect, 2)
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1