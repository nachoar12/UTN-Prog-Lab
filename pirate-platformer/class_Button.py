import pygame
from settings import TILE_SIZE


class Button():
    def __init__(self, x, y, image, screen):
        self.image = pygame.transform.scale(image, (TILE_SIZE * 3, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.screen = screen

    def draw(self):
        action = False
        # get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        self.screen.blit(self.image, self.rect)

        return action



