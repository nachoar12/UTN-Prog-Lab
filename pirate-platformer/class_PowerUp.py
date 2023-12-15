import pygame
from settings import TILE_SIZE


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (TILE_SIZE // 2, TILE_SIZE // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
