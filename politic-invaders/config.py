import pygame
import random

pygame.mixer.init()

# Dimensiones de la ventana del juego

ANCHO_VENTANA, ALTO_VENTANA = 1000, 800
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Politic Invaders")

# RELOJ - FPS , velocidad

FPS = 60
vel = 5

# Colores

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
NARANJA = (255, 128, 0)

COLORES_ENEMIGOS = [
    (0, 156, 222),  # celeste
    (117, 59, 189),  # violeta
    (254, 221, 0),  # amarillo
    (67, 72, 143),  # azul
    (249, 84, 97)  # rojo
]

COLOR_JUGADOR = (60, 179, 113)  # verde lima

# Tamaño de los bloques

TAMAÑO_BLOQUE = 40
FILA_ENEMIGOS = 5
COLUMNA_ENEMIGOS = 12
DISTANCIA_ENTRE_ENEMIGOS = 25
ANCHO_PROYECTIL = 25
ALTO_PROYECTIL = 30

# Fuente

pygame.font.init()
fuente_juego = pygame.font.SysFont("Arial", 28)
fuente_instrucciones = pygame.font.SysFont("Arial", 40)
fuente_game_over = pygame.font.SysFont("Arial", 32)

# sonidos
try:
    pygame.mixer.music.load(
        "politic-invaders/sounds/bgm.mp3")
    sonido_game_over_perder = pygame.mixer.Sound(
        "politic-invaders/sounds/game-over.mp3")
    sonido_game_over_ganar = pygame.mixer.Sound(
        "politic-invaders/sounds/success-trumpets.mp3")
    sonido_proyectiles = pygame.mixer.Sound(
        "politic-invaders/sounds/laser-shoot.mp3")
    sonido_pausa = pygame.mixer.Sound("politic-invaders/sounds/pause.mp3")
    sonido_colision = pygame.mixer.Sound("politic-invaders/sounds/crash.mp3")
    sonido_danio = pygame.mixer.Sound(
        "politic-invaders/sounds/classic_hurt.mp3")
except pygame.error as error:
    print("Error al cargar los sonidos")


# Número de vidas del jugador
VIDAS_JUGADOR = 3
enemigos_eliminados = 0

# Crear jugador
# Mascara jugador

CABILDO = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/cabildo.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))
JUGADOR = CABILDO
rect_jugador = JUGADOR.get_rect()
mascara_jugador = pygame.mask.from_surface(JUGADOR)


def crear_jugador():
    return {
        'x': ANCHO_VENTANA // 2 - TAMAÑO_BLOQUE // 2,
        'y': ALTO_VENTANA - TAMAÑO_BLOQUE * 1.5,
        'color': COLOR_JUGADOR,
        'mask': CABILDO
    }


# Crear enemigo

def crear_enemigo(x, y, color):

    return {'x': x, 'y': y, 'color': color, 'mask': None}
# Enemigos

# Mascaras enemigos

# dir_massa_img =
# dir_milei_img =
# dir_bulrich_img =
# dir_schiareti_img =
# dir_bregman_img =


MASSA = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Sergio_Massa_2019-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))
rect_massa = MASSA.get_rect()
mascara_massa = pygame.mask.from_surface(MASSA)

MILEI = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Javier_Milei-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))
rect_milei = MILEI.get_rect()
mascara_milei = pygame.mask.from_surface(MILEI)

BULRICH = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Bullrich-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))
rect_bulrich = BULRICH.get_rect()
mascara_bulrich = pygame.mask.from_surface(BULRICH)

SCHIARETTI = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/juan_schiaretti-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))
rect_schiaretti = SCHIARETTI.get_rect()
mascara_schiaretti = pygame.mask.from_surface(SCHIARETTI)

BREGMAN = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Myriam_Bregman-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))
rect_bregman = BREGMAN.get_rect()
mascara_bregman = pygame.mask.from_surface(BREGMAN)


# Crear matriz de enemigos
# Crear enemigos según el color


def crear_grilla_enemigos():
    enemigos = []
    for fila in range(FILA_ENEMIGOS):
        for col in range(COLUMNA_ENEMIGOS):
            x = col * (TAMAÑO_BLOQUE + DISTANCIA_ENTRE_ENEMIGOS)
            y = fila * (TAMAÑO_BLOQUE + DISTANCIA_ENTRE_ENEMIGOS)
            # Asigna un color específico a cada fila
            color = COLORES_ENEMIGOS[fila]
            enemigo = crear_enemigo(x, y, color)
            if enemigo["color"] == (0, 156, 222):  # celeste
                enemigo['mask'] = MASSA
            elif enemigo["color"] == (117, 59, 189):  # violeta
                enemigo['mask'] = MILEI
            elif enemigo["color"] == (254, 221, 0):  # amarillo
                enemigo['mask'] = BULRICH
            elif enemigo["color"] == (67, 72, 143):  # azul
                enemigo['mask'] = SCHIARETTI
            elif enemigo["color"] == (249, 84, 97):  # rojo
                enemigo['mask'] = BREGMAN

            enemigos.append(enemigo)
    return enemigos

# Crear proyectil


def crear_proyectil(x, y, color):
    return {'x': x, 'y': y, 'color': color, 'mask': None}

# Dibujar proyectiles


def dibujar_proyectiles(proyectiles):
    for proyectil in proyectiles:
        if proyectil['mask']:  # Verifica si hay una máscara asociada al proyectil
            ventana.blit(proyectil['mask'], (proyectil['x'], proyectil['y']))
        else:
            # Si no hay máscara, dibuja el proyectil con el color
            ancho_proyectil = ANCHO_PROYECTIL
            alto_proyectil = ALTO_PROYECTIL
            x_proyectil = proyectil['x'] - ancho_proyectil // 2
            y_proyectil = proyectil['y']
            pygame.draw.rect(ventana, proyectil['color'], (
                x_proyectil, y_proyectil, ancho_proyectil, alto_proyectil))


# Proyectiles jugador
# Mascara proyectil jugador


ARGENTINA = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/argentina-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
proyectil_jugador = ARGENTINA
rect_proyectil_jugador = ARGENTINA.get_rect()
mascara_jugador = pygame.mask.from_surface(ARGENTINA)

# Proyectiles enemigos
# Mascaras

CHORIPAN = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/choripan-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
rect_choripan = CHORIPAN.get_rect()
mascara_choripan = pygame.mask.from_surface(CHORIPAN)

DOLAR = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/dolar-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
rect_dolar = DOLAR.get_rect()
mascara_dolar = pygame.mask.from_surface(DOLAR)

VINO = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/vino-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
rect_vino = VINO.get_rect()
mascara_vino = pygame.mask.from_surface(VINO)

FERNET = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/fernet-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
rect_fernet = FERNET.get_rect()
mascara_fernet = pygame.mask.from_surface(FERNET)

BANDERIN = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/pañuelo-verde-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
rect_banderin = BANDERIN.get_rect()
mascara_banderin = pygame.mask.from_surface(BANDERIN)

# Función para que los enemigos disparen de manera aleatoria


def disparos_enemigos(enemigo, proyectiles):
    # Número aleatorio para simular la probabilidad de disparo
    probabilidad_disparo = random.randint(1, 2000)
    if probabilidad_disparo <= 5:  # 5% de probabilidad de disparo
        # Ajustar la posición del proyectil
        x = enemigo['x'] + TAMAÑO_BLOQUE // 2
        y = enemigo['y'] + TAMAÑO_BLOQUE
        proyectil = crear_proyectil(x, y, enemigo['color'])
        if enemigo["color"] == (0, 156, 222):  # celeste
            proyectil['mask'] = CHORIPAN
        elif enemigo["color"] == (117, 59, 189):  # violeta
            proyectil['mask'] = DOLAR
        elif enemigo["color"] == (254, 221, 0):  # amarillo
            proyectil['mask'] = VINO
        elif enemigo["color"] == (67, 72, 143):  # azul
            proyectil['mask'] = FERNET
        elif enemigo["color"] == (249, 84, 97):  # rojo
            proyectil['mask'] = BANDERIN
        proyectiles.append(proyectil)
