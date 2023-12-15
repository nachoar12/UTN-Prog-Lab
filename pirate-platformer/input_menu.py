import pygame
from pygame.locals import *

pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ingrese su nombre')

# Fuentes
font = pygame.font.Font(None, 36)
input_text = ''

def text_input():
    global input_text
    running = True
    while running:
        screen.fill(BLACK)
        text_surface = font.render("Ingrese su nombre y presione Enter:", True, WHITE)
        screen.blit(text_surface, (50, 50))

        input_rect = pygame.Rect(50, 150, 700, 40)
        pygame.draw.rect(screen, WHITE, input_rect, 2)

        text_surface = font.render(input_text, True, WHITE)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    return input_text

name = text_input()
print("El nombre ingresado es:", name)

pygame.quit()
