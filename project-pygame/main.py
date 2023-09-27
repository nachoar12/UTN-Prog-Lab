import pygame
from pygame.time import Clock
from pygame import display, time, draw, event
from config import *

# # lista -> [] -> mutable
# # tupla -> () -> inmutable

# l = [3, 4, 5]
# t = (3, 4, 5)

pygame.init()

is_running = True

CLOCK = pygame.time.Clock()
CLOCK = Clock()

RADIO = 100

# config de la pantalla principal
pygame.display.set_caption("Mileinator")
VENTANA = pygame.display.set_mode(SCREEN_SIZE)
VENTANA.fill((white))

while is_running:
    CLOCK.tick(FPS)
    for e in pygame.event.get():
        print(e)
        if e.type == pygame.QUIT:
            is_running = False
    
    circulo_central = draw.circle(VENTANA, yellow, CENTER_SCREEN , RADIO)
    draw.circle(VENTANA, red, (WIDTH - RADIO, RADIO) , RADIO)
    draw.circle(VENTANA, green, (RADIO, HEIGHT - RADIO ) , RADIO)


    draw.line(VENTANA, black, (0,0),(WIDTH, HEIGHT), 5)


    # ---> Actualizar pantalla
    pygame.display.flip()
    
pygame.quit()
    

   