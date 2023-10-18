import pygame
from aleatorias import generate_random_color, get_random_direction, create_blocks
from random import randint, randrange
from pygame.time import Clock
from config import *
from pygame.locals import *
from colisiones import *

# inicializar los modulos de pygame
pygame.init()


def terminar():
    pygame.quit()
    exit()


def mostrar_texto(texto, fuente, coordenadas, color_fuente, color_fondo):
    texto = fuente.render

    pass


def wait_user():
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                terminar()

            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    terminar()
                return


# config de la pantalla principal
pygame.display.set_caption("Game Test")
VENTANA = pygame.display.set_mode(SCREEN_SIZE)
VENTANA.fill((white))

# creo un reloj
CLOCK = pygame.time.Clock()
CLOCK = Clock()

# seteo sonidos
# coin_sound = pygame.mixer.Sound("./src/assets/'nombredelarchivo'")
# game_over_sound = pygame.mixer.Sound("./src/assets/'nombredelarchivo'")
# pygame.mixer.music.load("./src/assets/musica_fondo.mp3")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.1)
# print(pygame.mixer.music.get_volume())
playing_music = True

# cargar imagenes
# image_player = pygame.image.load("./src/assets/ovni")
# image_asteroid = pygame.image.load("./src/assets/asteroide")
# background = pygame.transform.scale(pygame.image.load("./src/assets/fondo"),SCREEN_SIZE)

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


def crear_bloque(imagen=None, left=0, top=0, width=BLOCK_WIDTH, height=BLOCK_HEIGHT, color=white, dir=3, borde=0, radio=-1, speed_x=5, speed_y=5,):
    rec = pygame.Rect(left, top, width, height)
    if imagen:
        imagen = pygame.transform.scale(imagen, (width, height))

    return {"rect": rec, "color": color, "dir": dir, "borde": borde, "radio": radio, "speed_x": speed_x, "speed_y": speed_y, "imagen": imagen}


def handler_new_coin():
    pass


def load_coin_list(coins, cantidad):
    for i in range(cantidad):
        size_coin = randint(size_min_coin, size_max_coin)
        coins.append(crear_bloque(None, randint(0, WIDTH - size_coin), randint(0,
                     HEIGHT - size_coin), size_coin, size_coin, yellow, radio=size_coin // 2))


def dibujar_asteroides(superficie, coins):
    for coin in coins:
        if coin["imagen"]:
            pass
    pass


# rectangulos
# creamos el bloque
bloques = []
# bloques = [{"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": generate_random_color(), "dir": get_random_direction()}]
block = crear_bloque()

for i in range(1):

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

# crear lista de coins
coins = []
# load_coins_list(coins,count_coins)

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
                move_left = False
            if e.key == pygame.K_LEFT or e.key == K_a:
                move_left = True
                move_right = False
            if e.key == pygame.K_DOWN or e.key == K_s:
                move_down = True
                move_up = False
            if e.key == pygame.K_UP or e.key == K_w:
                move_up = True
                move_down = False

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

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                new_coin = (crear_bloque(
                    e.pos[0], e.pos[1], size_coin, color=cyan, radio=size_coin // 2))
                new_coin["rect"].left -= size_coin // 2
                new_coin["rect"].top -= size_coin // 2
                coins.append(new_coin)
            if e.button == 3:
                block["rect"].center = CENTER_SCREEN

    # dibujo formas geometricas

    # circulo_central = draw.circle(VENTANA, yellow, CENTER_SCREEN , RADIO)
    # draw.circle(VENTANA, red, (WIDTH - RADIO, RADIO) , RADIO)
    # draw.circle(VENTANA, green, (RADIO, HEIGHT - RADIO ) , RADIO)
    # draw.line(VENTANA, black, (0,0),(WIDTH, HEIGHT), 5)

    # -----> Actualizar elementos
    # controlo rebotes y cambio de direccion
    # for block in bloques:
    #     # rebote derecha pantalla
    #     if block["rect"].right >= WIDTH:
    #         if block["dir"] == DOWNRIGHT:
    #             block["dir"] = DOWNLEFT
    #         elif block["dir"] == UPRIGHT:
    #             block["dir"] = UPLEFT
    #     # rebote izquierda pantalla
    #     elif block["rect"].left <= 0:
    #         if block["dir"] == DOWNLEFT:
    #             block["dir"] = DOWNRIGHT
    #         elif block["dir"] == UPLEFT:
    #             block["dir"] = UPRIGHT
    #     # rebote abajo pantalla
    #     elif block["rect"].bottom >= HEIGHT:
    #         if block["dir"] == DOWNLEFT:
    #             block["dir"] = UPLEFT
    #         elif block["dir"] == DOWNRIGHT:
    #             block["dir"] = UPRIGHT
    #     # rebote arriba pantalla
    #     elif block["rect"].top <= 0:
    #         if block["dir"] == UPLEFT:
    #             block["dir"] = DOWNLEFT
    #         elif block["dir"] == UPRIGHT:
    #             block["dir"] = DOWNRIGHT

    for block in bloques:
        # muevo el rectangulo de acuerdo a la direccion
        if move_right and block["rect"].right <= (WIDTH - SPEED):
            # DERECHA
            block["rect"].left += speed_x
        elif move_left and block["rect"].left >= (0 + SPEED):
            # IZQUIERDA
            block["rect"].left -= speed_x
        elif move_up and block["rect"].top >= (0 + SPEED):
            # ARRIBA
            block["rect"].top -= speed_y
        elif move_down and block["rect"].bottom <= (HEIGHT - SPEED):
            # ABAJO
            block["rect"].top += speed_y

        # movemos los asteroides

        for coin in coins:
            coin["rect"].move_ip(0, coin["speed_y"])

        # reaparecerlos desde arriba de la pantalla

        for coin in coins:
            coin["rect"].move_ip(0, - size_coin)

    for coin in coins[:]:
        if coin["imagen"]:
            VENTANA.blit(coin["imagen"], coin["rect"])
        else:
            # pygame.draw.rect()
            # if detectar_colision_circ(coin["rect"], block["rect"]):
            #     coins.remove(coin)
            #     contador += 1
            #     # texto = fuente.render(f"Coins : {contador}", True, magenta)
            #     # rect_texto = texto.get_rect()
            #     # rect_texto.midtop =

            # VENTANA.blit(coin["imagen", coin ["rect"]])
            pass

    # -----> Dibujar pantalla

    VENTANA.fill(black)
    for coin in coins:
        pygame.draw.rect(VENTANA, coin["color"],
                         coin["rect"], coin["borde", coin["radio"]])

    for block in bloques:
        pygame.draw.rect(VENTANA, block["color"], block["rect"])

    # -----> Actualizar pantalla
    pygame.display.flip()

pygame.quit()
