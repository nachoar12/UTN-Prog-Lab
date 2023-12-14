import pygame
from settings import TILE_SIZE


class Key():
    def __init__(self, x, y, image, screen):
        self.image = pygame.transform.scale(image, (TILE_SIZE * 1.5, TILE_SIZE * 1.5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)
