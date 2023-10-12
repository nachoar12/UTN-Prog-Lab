import pygame
from aleatorias import generate_random_color, get_random_direction, create_blocks
from random import randint, randrange
from pygame.time import Clock
from config import *

# inicializar los modulos de pygame
pygame.init()

# config de la pantalla principal
pygame.display.set_caption("Game Test")
VENTANA = pygame.display.set_mode(SCREEN_SIZE)
VENTANA.fill((white))

# creo un reloj
CLOCK = pygame.time.Clock()
CLOCK = Clock()

# evento personalizado
EVENT_NEW_COIN = pygame.USEREVENT + 1

pygame.time.set_timer(EVENT_NEW_COIN, 3000)

contador = 0
contador_gde = 0

# movimiento


# rectangulos
bloques = []
# bloques = [{"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()}]

for i in range(5):

    rect = pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH),
                       randint(0, HEIGHT - BLOCK_HEIGHT),
                       BLOCK_WIDTH,
                       BLOCK_HEIGHT)
    color = generate_random_color()
    dir = get_random_direction()
    speed_x = randint(5, 15)
    speed_y = randint(5, 15)

    block_dict = {"rect": rect, "color": color,
                  "dir": dir, "speed_x": speed_x, "speed_y": speed_y}
    bloques.append(block_dict)

is_running = True

while is_running:
    CLOCK.tick(FPS)
    # -----> Detectar los eventos
    for e in pygame.event.get():
        # print(e)
        if e.type == pygame.QUIT:
            is_running = False

        if e.type == EVENT_NEW_COIN:
            pass

    # -----> Actualizar elementos
    # controlo rebotes y cambio de direccion
    for block in bloques:
        # rebote derecha pantalla
        if block["rect"].right >= WIDTH:
            if block["dir"] == DOWNRIGHT:
                block["dir"] = DOWNLEFT
            elif block["dir"] == UPRIGHT:
                block["dir"] = UPLEFT
            block["color"] = generate_random_color()
        # rebote izquierda pantalla
        elif block["rect"].left <= 0:
            if block["dir"] == DOWNLEFT:
                block["dir"] = DOWNRIGHT
            elif block["dir"] == UPLEFT:
                block["dir"] = UPRIGHT
            block["color"] = generate_random_color()
        # rebote abajo pantalla
        elif block["rect"].bottom >= HEIGHT:
            if block["dir"] == DOWNLEFT:
                block["dir"] = UPLEFT
            elif block["dir"] == DOWNRIGHT:
                block["dir"] = UPRIGHT
            block["color"] = generate_random_color()
        # rebote arriba pantalla
        elif block["rect"].top <= 0:
            if block["dir"] == UPLEFT:
                block["dir"] = DOWNLEFT
            elif block["dir"] == UPRIGHT:
                block["dir"] = DOWNRIGHT
            block["color"] = generate_random_color()

    for block in bloques:
        # muevo el rectangulo de acuerdo a la direccion
        if block["dir"] == DOWNRIGHT:
            # DERECHA
            block["rect"].left += speed_x
            block["rect"].top += speed_y
        elif block["dir"] == DOWNLEFT:
            # IZQUIERDA
            block["rect"].left -= speed_x
            block["rect"].top += speed_y
        elif block["dir"] == UPLEFT:
            # ARRIBA
            block["rect"].left -= speed_x
            block["rect"].top -= speed_y
        elif block["dir"] == UPRIGHT:
            # ABAJO
            block["rect"].left += speed_x
            block["rect"].top -= speed_y

    # -----> Dibujar pantalla
    VENTANA.fill(black)
    for block in bloques:
        pygame.draw.rect(VENTANA, block["color"], block["rect"])

    # -----> Actualizar pantalla
    pygame.display.flip()

pygame.quit()
