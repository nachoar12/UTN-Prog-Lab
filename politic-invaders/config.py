import pygame
import os

# Se importan las librerías necesarias para el juego.

# Creo la funcion para cerrar el juego en caso de error.


def cerrar_juego():
    """
    Cierra el juego y sale de la aplicación.
    """
    print("Cerrando juego...")
    pygame.quit()
    exit()


# Se obtiene y muestra la ruta actual del directorio.
dir_actual = os.getcwd()
dir_actual = os.path.abspath(dir_actual)
print(dir_actual)

# Se inicializa el módulo de mezcla de sonido de Pygame.
pygame.mixer.init()

# Se establecen las dimensiones de la ventana del juego.
ANCHO_VENTANA, ALTO_VENTANA = 900, 700  # tamaño original 1000 x 800
CENTRO_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Politic Invaders")

# Se establecen los parámetros relacionados con el tiempo y la velocidad.
FPS = 60  # Cuadros por segundo.
velocidad_jugador = 5  # Velocidad del juego.
velocidad_enemigos = 1
probabilidad_disparo_enemigo = 1

# Se definen los colores utilizados en el juego.
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
NARANJA = (255, 128, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CELESTE = (125, 174, 217)
AMARILLO = (236, 184, 64)
COLORES_ENEMIGOS = [
    (0, 156, 222),  # celeste
    (117, 59, 189),  # violeta
    (254, 221, 0),  # amarillo
    (67, 72, 143),  # azul
    (249, 84, 97)  # rojo
]
COLOR_JUGADOR = (60, 179, 113)  # verde lima

# Se establecen las dimensiones de los bloques y proyectiles.
TAMAÑO_BLOQUE = 40
FILA_ENEMIGOS = 5
COLUMNA_ENEMIGOS = 10
DISTANCIA_ENTRE_ENEMIGOS = 25
ANCHO_PROYECTIL = 25
ALTO_PROYECTIL = 30

# Se inicializan las fuentes utilizadas en el juego.
pygame.font.init()
fuente_juego = pygame.font.SysFont("Arial", 26)
fuente_instrucciones = pygame.font.SysFont("Arial", 34)  # tamaño original 40
fuente_game_over = pygame.font.SysFont("Arial", 32)

icono = pygame.Surface((20, 20))
icono = icono.convert_alpha()
icono.fill((NEGRO))

try:
    # Se carga la imagen de fondo del juego, menues e icono
    imagen_bkg = pygame.transform.scale(pygame.image.load(
        "politic-invaders/images/espacio.jpg"), (ANCHO_VENTANA, ALTO_VENTANA))
    menu_bkg = pygame.transform.scale(pygame.image.load(
        "politic-invaders/images/argentina-8-bit.jpg"), (ANCHO_VENTANA, ALTO_VENTANA))
    instrucciones_bkg = pygame.transform.scale(pygame.image.load(
        "politic-invaders/images/planeta-tierra.png"), (ANCHO_VENTANA, ALTO_VENTANA))
    game_over_bkg = pygame.transform.scale(pygame.image.load(
        "politic-invaders/images/game-over.png"), (ANCHO_VENTANA, ALTO_VENTANA))
    game_over_win_bkg = pygame.transform.scale(pygame.image.load(
        "politic-invaders/images/game-over-win.png"), (ANCHO_VENTANA, ALTO_VENTANA))
    icono = pygame.transform.scale(pygame.image.load(
        "politic-invaders/images/icon.png"), (20, 20))
except ValueError as error:
    print("Error al cargar los sonidos: ")
    print(error)
    cerrar_juego()


pygame.display.set_icon(icono)


# Se cargan y se inicializan los sonidos del juego.
# En caso de error al cargar los sonidos, se imprime un mensaje.

try:
    pygame.mixer.music.load("politic-invaders/sounds/bgm.mp3")
    sonido_game_over_perder = pygame.mixer.Sound(
        "politic-invaders/sounds/game-over.mp3")
    sonido_game_over_ganar = pygame.mixer.Sound(
        "politic-invaders/sounds/success-trumpets.mp3")
    sonido_proyectiles = pygame.mixer.Sound(
        "politic-invaders/sounds/laser-shoot.mp3")
    sonido_pausa = pygame.mixer.Sound("politic-invaders/sounds/pause.mp3")
    sonido_colision = pygame.mixer.Sound("politic-invaders/sounds/crash.mp3")
    sonido_colision.set_volume(0.5)
    sonido_danio = pygame.mixer.Sound(
        "politic-invaders/sounds/classic_hurt.mp3")
    sonido_vida = pygame.mixer.Sound(
        "politic-invaders/sounds/vida_extra.mp3")
    sonido_vida.set_volume(0.5)
    sonido_massa = pygame.mixer.Sound(
        "politic-invaders/sounds/no-me-quemes.mp3")
    sonido_milei = pygame.mixer.Sound(
        "politic-invaders/sounds/afuera-milei.mp3")
    sonido_bulrich = pygame.mixer.Sound(
        "politic-invaders/sounds/viejos-meados-pato-bullrich.mp3")
    sonido_schiaretti = pygame.mixer.Sound(
        "politic-invaders/sounds/schiaretti.mp3")
    sonido_bregman = pygame.mixer.Sound(
        "politic-invaders/sounds/gatito-mimoso-myriam-bregman.mp3")
except ValueError as error:
    print("Error al cargar los sonidos: ")
    print(error)
    cerrar_juego()


# Se establece el número de vidas del jugador y los enemigos eliminados en 0.
VIDAS_JUGADOR = 3
enemigos_eliminados = 0

# Se intenta cargar el archivo de puntuación máxima (highscore.txt) y se verifica en caso que exista que no este vacío.
# En caso que el archivo no contenga información, se asigna un max_score de 0.
# En caso de error, se asigna un max_score de 0 y se muestra un mensaje de error.
try:
    with open("politic-invaders/highscore.txt", "r") as highscore_data:
        if highscore_data.readline() != "" or None:
            max_score = highscore_data.readline()
        else:
            max_score = 0
except ValueError as error:
    print(error)
    max_score = 0

# Se cargan y se establecen las máscaras de los jugadores y enemigos.
# Aquí se realizan las transformaciones y se generan las máscaras a partir de las imágenes.

CABILDO = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/cabildo.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))
JUGADOR = CABILDO
rect_jugador = JUGADOR.get_rect()
mascara_jugador = pygame.mask.from_surface(JUGADOR)

VIDA = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/vida.png"), (TAMAÑO_BLOQUE // 1.5, TAMAÑO_BLOQUE // 1.5))
rect_vida = VIDA.get_rect()
mascara_vida = pygame.mask.from_surface(VIDA)

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


# Enemigos y proyectiles - Máscaras

# Máscaras para los proyectiles del jugador
ARGENTINA = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/argentina-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
proyectil_jugador = ARGENTINA
rect_proyectil_jugador = ARGENTINA.get_rect()
mascara_proyectil_jugador = pygame.mask.from_surface(ARGENTINA)

# Máscaras para los proyectiles de los enemigos
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
