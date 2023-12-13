import pygame
from settings import TILE_SIZE


class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(
            './assets/img/traps/spikes.png'), (TILE_SIZE, TILE_SIZE // 1.3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
