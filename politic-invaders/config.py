import pygame
import random

# Dimensiones de la ventana del juego

ANCHO_VENTANA, ALTO_VENTANA = 1000, 800
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Politic Invaders")

# RELOJ - FPS
FPS = 60

# Colores
NEGRO = (0, 0, 0)
COLORES_ENEMIGOS = [
    (0, 156, 222),  # celeste
    (117, 59, 189),  # violeta
    (254, 221, 0),  # amarillo
    (67, 72, 143),  # azul
    (249, 84, 97)  # rojo
]


COLOR_JUGADOR = (60, 179, 113)  # verde lima

# Tamaño de los bloques
TAMAÑO_BLOQUE = 60
FILA_ENEMIGOS = 5
COLUMNA_ENEMIGOS = 10
DISTANCIA_ENTRE_ENEMIGOS = 25
ANCHO_PROYECTIL = 30
ALTO_PROYECTIL = 40

# Crear jugador


def crear_jugador():
    return {
        'x': ANCHO_VENTANA // 2 - TAMAÑO_BLOQUE // 2,
        'y': ALTO_VENTANA - TAMAÑO_BLOQUE * 2,
        'color': COLOR_JUGADOR
    }

# Enemigos


MASSA = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Sergio_Massa_2019-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))

CHORIPAN = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Sergio_Massa_2019-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))

MILEI = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Javier_Milei-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))

BULRICH = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Bullrich-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))

SCHIARETTI = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/juan_schiaretti-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))

BREGMAN = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/Myriam_Bregman-removebg-preview.png"), (TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))

# Crear enemigos según el color


def crear_enemigo(x, y, color):
    return {'x': x, 'y': y, 'color': color, 'mask': None}

# Dibujar bloque


def dibujar_bloque(block):
    pygame.draw.rect(ventana, block['color'], (block['x'],
                     block['y'], TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))

# Crear matriz de enemigos


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


# Dibujar enemigos


def dibujar_enemigos(enemigos):
    for enemigo in enemigos:
        # dibujar_bloque(enemigo)  # Draw the block
        if enemigo['mask']:  # Check if there's a mask image
            # Draw the mask image at enemy position
            ventana.blit(enemigo['mask'], (enemigo['x'], enemigo['y']))

# Mover jugador


def mover_jugador(tecla, jugador, vel):
    if tecla[pygame.K_LEFT] and jugador['x'] > vel:
        jugador['x'] -= vel
    if tecla[pygame.K_RIGHT] and jugador['x'] < ANCHO_VENTANA - TAMAÑO_BLOQUE - vel:
        jugador['x'] += vel


# Crear una función para mover los enemigos
def mover_enemigos(enemigos, sentido_movimiento):
    for enemigo in enemigos:
        enemigo['x'] += sentido_movimiento * 3

        if enemigo['x'] >= ANCHO_VENTANA - TAMAÑO_BLOQUE or enemigo['x'] <= 0:
            for e in enemigos:
                e['y'] += 15  # Descenso de 15 píxeles
            sentido_movimiento *= -1  # Invertir el sentido para el siguiente movimiento en X
            break  # Salir del bucle, solo cambiar una vez el sentido

    return sentido_movimiento

# Crear proyectil


def crear_proyectil(x, y, color):
    return {'x': x, 'y': y, 'color': color, 'mask': None}

# Dibujar proyectil


def dibujar_proyectil(proyectil):
    # Cambiar el tamaño según sea necesario
    ancho_proyectil = ANCHO_PROYECTIL
    alto_proyectil = ALTO_PROYECTIL
    pygame.draw.rect(
        ventana, proyectil['color'], (proyectil['x'] - ancho_proyectil // 2, proyectil['y'], ancho_proyectil, alto_proyectil))

# Función para disparar


def disparar_proyectil(jugador, proyectiles):
    x = jugador['x'] + TAMAÑO_BLOQUE // 2   # Ajustar la posición del proyectil
    y = jugador['y']
    proyectil = crear_proyectil(x, y, jugador['color'])
    proyectiles.append(proyectil)

# Función para mover proyectiles


def mover_proyectiles_jugador(proyectiles):
    for proyectil in proyectiles:
        proyectil['y'] -= 5  # Ajustar la velocidad del proyectil

# Función para dibujar proyectiles


# Dibujar proyectiles
def dibujar_proyectiles(proyectiles):
    for proyectil in proyectiles:
        if proyectil['mask']:  # Verifica si hay una máscara asociada al proyectil
            ventana.blit(proyectil['mask'], (proyectil['x'], proyectil['y']))
        else:
            # Si no hay máscara, dibuja el proyectil con el color
            ancho_proyectil = ANCHO_PROYECTIL
            alto_proyectil = ALTO_PROYECTIL
            pygame.draw.rect(ventana, proyectil['color'], (
                proyectil['x'] - ancho_proyectil // 2, proyectil['y'], ancho_proyectil, alto_proyectil))
# Proyectiles enemigos


CHORIPAN = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/choripan-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
DOLAR = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/dolar-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
VINO = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/vino-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
FERNET = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/fernet-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))
BANDERIN = pygame.transform.scale(pygame.image.load(
    "politic-invaders/images/pañuelo-verde-removebg-preview.png"), (ANCHO_PROYECTIL, ALTO_PROYECTIL))

# Crear función para disparo de enemigos de manera aleatoria


def disparar_enemigo(enemigo, proyectiles):
    # Generar un número aleatorio para simular la probabilidad de disparo
    probabilidad_disparo = random.randint(1, 2000)
    if probabilidad_disparo <= 5:  # Por ejemplo, 5% de probabilidad de disparo
        x = enemigo['x'] + TAMAÑO_BLOQUE // 2 - \
            5  # Ajustar la posición del proyectil
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

# Función para que los enemigos disparen proyectiles hacia abajo


def enemigos_disparan(enemigos, proyectiles):
    for enemigo in enemigos:
        disparar_enemigo(enemigo, proyectiles)

# Función para mover proyectiles hacia abajo


def mover_proyectiles_enemigos(proyectiles):
    for proyectil in proyectiles:
        proyectil['y'] += 5  # Mover hacia abajo


# Número de vidas del jugador
VIDAS_JUGADOR = 5
enemigos_eliminados = 0

# Función para detectar colisiones entre dos rectángulos


def detectar_colision(rect1, rect2):
    return rect1.colliderect(rect2)

# Función para actualizar las vidas del jugador


def actualizar_vidas_jugador(vidas):
    if vidas <= 0:
        return 0
    else:
        return vidas - 1


pygame.font.init()
fuente = pygame.font.SysFont("Arial", 24)

# Pantalla Game Over


def ventana_game_over():
    texto_game_over = fuente.render("Game Over", True, (255, 255, 255))
    texto_estadisticas = fuente.render(
        f"Enemigos eliminados: {enemigos_eliminados}", True, (255, 255, 255))
    texto_reinicio = fuente.render(
        "Presiona R para reiniciar", True, (255, 255, 255))

    ventana.fill((0, 0, 0))  # Clear the screen
    ventana.blit(texto_game_over, (ANCHO_VENTANA //
                 2 - 100, ALTO_VENTANA // 2 - 50))
    ventana.blit(texto_estadisticas,
                 (ANCHO_VENTANA // 2 - 120, ALTO_VENTANA // 2))
    ventana.blit(texto_reinicio, (ANCHO_VENTANA //
                 2 - 150, ALTO_VENTANA // 2 + 50))
    pygame.display.update()
