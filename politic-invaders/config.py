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


# Se inicializa el módulo de mezcla de sonido de Pygame.
pygame.mixer.init()

TITULO_JUEGO = "Politic invaders v1.0"

# Se establecen las dimensiones de la ventana del juego.
ANCHO_VENTANA, ALTO_VENTANA = 900, 700  # tamaño original 1000 x 800
CENTRO_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption(TITULO_JUEGO)

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
fuente_juego = pygame.font.SysFont("Arial", 22)
fuente_instrucciones = pygame.font.SysFont("Arial", 34)  # tamaño original 40
fuente_game_over = pygame.font.SysFont("Arial", 32)

icono = pygame.Surface((20, 20))
icono = icono.convert_alpha()
icono.fill((NEGRO))


# Obtengo la ruta del directorio actual
dir_actual = os.path.abspath(os.getcwd())

# Defino la ruta base para la carpeta de imágenes
ruta_imagenes = os.path.join(dir_actual, "politic-invaders", "images")

# Defino las rutas completas a las imágenes uniendo la ruta base con el nombre de las imagenes
ruta_espacio = os.path.join(ruta_imagenes, "espacio.jpg")
ruta_argentina_8bit = os.path.join(ruta_imagenes, "argentina-8-bit.jpg")
ruta_planeta_tierra = os.path.join(ruta_imagenes, "planeta-tierra.png")
ruta_game_over = os.path.join(ruta_imagenes, "game-over.png")
ruta_game_over_win = os.path.join(ruta_imagenes, "game-over-win.png")
ruta_icono = os.path.join(ruta_imagenes, "icon.png")

# Intento cargar las imágenes utilizando las rutas completas
try:
    imagen_bkg = pygame.transform.scale(pygame.image.load(
        ruta_espacio), (ANCHO_VENTANA, ALTO_VENTANA))
    menu_bkg = pygame.transform.scale(pygame.image.load(
        ruta_argentina_8bit), (ANCHO_VENTANA, ALTO_VENTANA))
    instrucciones_bkg = pygame.transform.scale(pygame.image.load(
        ruta_planeta_tierra), (ANCHO_VENTANA, ALTO_VENTANA))
    game_over_bkg = pygame.transform.scale(pygame.image.load(
        ruta_game_over), (ANCHO_VENTANA, ALTO_VENTANA))
    game_over_win_bkg = pygame.transform.scale(pygame.image.load(
        ruta_game_over_win), (ANCHO_VENTANA, ALTO_VENTANA))
    icono = pygame.transform.scale(pygame.image.load(ruta_icono), (20, 20))
except FileNotFoundError as file_error:
    print("Archivo no encontrado: ", file_error)
    cerrar_juego()
except pygame.error as pygame_error:
    print("Error de pygame: ", pygame_error)
    cerrar_juego()
except Exception as error:
    print("Error : ", error)
    cerrar_juego()


pygame.display.set_icon(icono)


# Se cargan y se inicializan los sonidos del juego.
# En caso de error al cargar los sonidos, se imprime un mensaje y se cierra el juego.

ruta_sonidos = os.path.join(dir_actual, "politic-invaders", "sounds")

try:
    pygame.mixer.music.load(os.path.join(ruta_sonidos, "bgm.mp3"))
    pygame.mixer.music.set_volume(0.5)
    sonido_game_over_perder = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "game-over.mp3"))
    sonido_game_over_ganar = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "success-trumpets.mp3"))
    sonido_proyectiles = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "laser-shoot.mp3"))
    sonido_proyectiles.set_volume(0.4)
    sonido_pausa = pygame.mixer.Sound(os.path.join(ruta_sonidos, "pause.mp3"))
    sonido_colision = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "crash.mp3"))
    sonido_colision.set_volume(0.3)
    sonido_danio = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "classic_hurt.mp3"))
    sonido_vida = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "vida_extra.mp3"))
    sonido_vida.set_volume(0.4)
    sonido_massa = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "no-me-quemes.mp3"))
    sonido_milei = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "afuera-milei.mp3"))
    sonido_bulrich = pygame.mixer.Sound(os.path.join(
        ruta_sonidos, "viejos-meados-pato-bullrich.mp3"))
    sonido_schiaretti = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "schiaretti.mp3"))
    sonido_bregman = pygame.mixer.Sound(os.path.join(
        ruta_sonidos, "gatito-mimoso-myriam-bregman.mp3"))
    sonido_tiemblen = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "tiemblen.mp3"))
    sonido_tiemblen.set_volume(0.3)
    sonido_motosierra = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "motosierra.mp3"))
    sonido_toasty = pygame.mixer.Sound(
        os.path.join(ruta_sonidos, "toasty.mp3"))
except FileNotFoundError as file_error:
    print("Archivo no encontrado: ", file_error)
    cerrar_juego()
except pygame.error as pygame_error:
    print("Error de pygame: ", pygame_error)
    cerrar_juego()
except Exception as error:
    print("Error : ", error)
    cerrar_juego()


# Se establece el número de vidas del jugador y los enemigos eliminados en 0.
VIDAS_JUGADOR = 3
enemigos_eliminados = 0

# Se intenta cargar el archivo de puntuación máxima (highscore.txt) y se verifica en caso que exista que no este vacío.
# En caso que el archivo no contenga información, se asigna un max_score de 0.
# En caso de error, se asigna un max_score de 0 y se muestra un mensaje de error.
try:
    with open("politic-invaders/highscore.txt", "r") as highscore_data:
        # Lee la primera línea y elimina espacios en blanco
        max_score = highscore_data.readline().strip()
        if not max_score:  # Verifica si max_score está vacío después de eliminar espacios en blanco
            max_score = 0
        else:
            max_score = int(max_score)  # Convierte a entero si no está vacío
except FileNotFoundError as file_error:
    print("Archivo no encontrado: ", file_error)
    cerrar_juego()
except ValueError as value_error:
    print("Error de valor: ", value_error)
    cerrar_juego()
except IOError as io_error:
    print("Error de E/S: ", io_error)
    cerrar_juego()


# MASCARAS

# JUGADOR

JUGADOR = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/cabildo.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))
rect_jugador = JUGADOR.get_rect()
mascara_jugador = pygame.mask.from_surface(JUGADOR)

# POWER UPS

VIDA = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/vida.png"), (TAMAÑO_BLOQUE // 1.5, TAMAÑO_BLOQUE // 1.5))
rect_vida = VIDA.get_rect()
mascara_vida = pygame.mask.from_surface(VIDA)

MOTOSIERRA = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Milei-motosierra.png"), (TAMAÑO_BLOQUE * 2, TAMAÑO_BLOQUE * 1.5))
rect_motosierra = MOTOSIERRA.get_rect()
mascara_motosierra = pygame.mask.from_surface(MOTOSIERRA)

MOTOSIERRA_POWER = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Milei-motosierra.png"), (ANCHO_VENTANA // 2, ALTO_VENTANA - TAMAÑO_BLOQUE - 35))
rect_motosierra_power = MOTOSIERRA_POWER.get_rect()
mascara_motosierra_power = pygame.mask.from_surface(MOTOSIERRA_POWER)

PERON = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/peron-2.png"), (TAMAÑO_BLOQUE * 2.5, TAMAÑO_BLOQUE * 2.5))
rect_peron = PERON.get_rect()
mascara_peron = pygame.mask.from_surface(PERON)

# ENEMIGOS

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


# PROYECTILES

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
