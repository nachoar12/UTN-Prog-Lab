import pygame
from settings import *


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(
            './assets/img/door/door.png'), (TILE_SIZE * 1.3, TILE_SIZE * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
