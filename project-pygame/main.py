import pygame
from aleatorias import generate_random_color, get_random_direction, create_blocks
from random import randint
from pygame.time import Clock

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
pygame.display.set_caption("Game Test")
VENTANA = pygame.display.set_mode(SCREEN_SIZE)
VENTANA.fill((white))

# direcciones
UPRIGHT = 9
DOWNRIGHT = 3
DOWNLEFT = 1
UPLEFT = 7

# dimensiones del rectangulo
BLOCK_WIDTH = 25
BLOCK_HEIGHT = 25


# rectangulos
bloques = []
# bloques = [{"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()}]

for i in range(40):

        rect = pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT)
        color = generate_random_color()
        dir = get_random_direction()

        block_dict = {"rect": rect, "color": color, "dir": dir}
        bloques.append(block_dict)
    

while is_running:
    CLOCK.tick(FPS)
    # -----> Detectar los eventos
    for e in pygame.event.get():
        # print(e)
        if e.type == pygame.QUIT:
            is_running = False
    
    # dibujo formas geometricas

    # circulo_central = draw.circle(VENTANA, yellow, CENTER_SCREEN , RADIO)
    # draw.circle(VENTANA, red, (WIDTH - RADIO, RADIO) , RADIO)
    # draw.circle(VENTANA, green, (RADIO, HEIGHT - RADIO ) , RADIO)
    # draw.line(VENTANA, black, (0,0),(WIDTH, HEIGHT), 5)

    # -----> Actualizar elementos
    # controlo rebotes y cambio de direccion
    for block in bloques:
        # rebotre derecha pantalla
        if block["rect"].right >= WIDTH:
            if block["dir"] == DOWNRIGHT:
                block["dir"] = DOWNLEFT
            elif block["dir"] == UPRIGHT:
                block["dir"] = UPLEFT
        # rebote izquierda pantalla
        elif block["rect"].left <= 0:
            if block["dir"] == DOWNLEFT:
                block["dir"] = DOWNRIGHT
            elif block["dir"] == UPLEFT:
                block["dir"] = UPRIGHT
        # rebote abajo pantalla
        elif block["rect"].bottom >= HEIGHT:
            if block["dir"] == DOWNLEFT:
                block["dir"] = UPLEFT
            elif block["dir"] == DOWNRIGHT:
                block["dir"] = UPRIGHT
        # rebote arriba pantalla
        elif block["rect"].top <= 0:
            if block["dir"] == UPLEFT:
                block["dir"] = DOWNLEFT
            elif block["dir"] == UPRIGHT:
                block["dir"] = DOWNRIGHT

    for block in bloques:
        # muevo el rectangulo de acuerdo a la direccion
        if block["dir"] == DOWNRIGHT:
            block["rect"].left += SPEED
            block["rect"].top += SPEED
        elif block["dir"] == DOWNLEFT:
            block["rect"].left -= SPEED
            block["rect"].top += SPEED
        elif block["dir"] == UPLEFT:
            block["rect"].left -= SPEED
            block["rect"].top -= SPEED
        elif block["dir"] == UPRIGHT:
            block["rect"].left += SPEED
            block["rect"].top -= SPEED

    # -----> Dibujar pantalla
    VENTANA.fill(black)
    for block in bloques:
        pygame.draw.rect(VENTANA, block["color"], block["rect"])

    # -----> Actualizar pantalla
    pygame.display.flip()
    
pygame.quit()
    

   