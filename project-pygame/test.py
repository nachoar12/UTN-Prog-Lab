import pygame
from aleatorias import generate_random_color, get_random_direction, create_blocks
from random import randint, randrange
from pygame.time import Clock
from config import *
from pygame.locals import *

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

move_left = False
move_right = False
move_down = False
move_up = False



# rectangulos
bloques = []
# bloques = [{"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()}]

for i in range(1):

        rect = pygame.Rect( randint(0, WIDTH - BLOCK_WIDTH),
                            randint(0, HEIGHT - BLOCK_HEIGHT), 
                            BLOCK_WIDTH, 
                            BLOCK_HEIGHT)
        color = generate_random_color()
        dir = get_random_direction()
        speed_x = randint(5,15)
        speed_y = randint(5,15)

        block_dict = {"rect": rect, "color": color, "dir": dir, "speed_x": speed_x, "speed_y": speed_y}
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
        
        # evento al presionar la tecla
        if e.type == pygame.KEYDOWN:
            # teclas de movimiento WASD y flechas
            if e.key == pygame.K_RIGHT or e.key == K_d:
                move_right = True
            if e.key == pygame.K_LEFT or e.key == K_a:
                move_left = True
            if e.key == pygame.K_DOWN or e.key == K_s:
                move_down = True
            if e.key == pygame.K_UP or e.key == K_w:
                move_up = True

        # evento al soltar la tecla
        if e.type == pygame.KEYUP:
            # teclas de movimiento WASD y flechas
            if e.key == pygame.K_RIGHT or e.key == K_d:
                move_right = False
            if e.key == pygame.K_LEFT or e.key == K_a:
                move_left = False
            if e.key == pygame.K_DOWN or e.key == K_s:
                move_down = False
            if e.key == pygame.K_UP or e.key == K_w:
                move_up = False
            # tecla para cerrar el juego Esc
            if e.key == K_ESCAPE:
                is_running = False

            

    # dibujo formas geometricas

    # circulo_central = draw.circle(VENTANA, yellow, CENTER_SCREEN , RADIO)
    # draw.circle(VENTANA, red, (WIDTH - RADIO, RADIO) , RADIO)
    # draw.circle(VENTANA, green, (RADIO, HEIGHT - RADIO ) , RADIO)
    # draw.line(VENTANA, black, (0,0),(WIDTH, HEIGHT), 5)

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
        if move_right:
            # DERECHA
            block["rect"].left += speed_x
        elif move_left:
            # IZQUIERDA
            block["rect"].left -= speed_x
        elif move_up:
            # ARRIBA
            block["rect"].top -= speed_y
        elif move_down:
            # ABAJO
            block["rect"].top += speed_y

    # -----> Dibujar pantalla
    VENTANA.fill(black)
    for block in bloques:
        pygame.draw.rect(VENTANA, block["color"], block["rect"])

    # -----> Actualizar pantalla
    pygame.display.flip()
    
pygame.quit()
    

   