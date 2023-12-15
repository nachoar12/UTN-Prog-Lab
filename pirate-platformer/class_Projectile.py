import pygame
from settings import SCREEN_WIDTH

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, image_path, width, height, speed=8):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = speed
        self.image_right = self.image
        self.image_left = pygame.transform.flip(self.image, True, False)

    def update(self):
        self.rect.x += self.speed * self.direction
        
        if self.rect.x < 0 - self.width or self.rect.x > SCREEN_WIDTH + self.width:
            self.kill() 

        # image direction
        if self.direction == 1:  
            self.image = self.image_right
        elif self.direction == -1:  
            self.image = self.image_left