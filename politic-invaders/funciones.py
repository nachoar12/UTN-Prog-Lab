import pygame
from config import *

# Funciones

# Cerrar juego


def cerrar_juego():
    print("Cerrando juego")
    pygame.quit()
    exit()

# Esperar usuario


def esperar_usuario():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    cerrar_juego()
                return


# Dibujar bloque


def dibujar_bloque(block):
    pygame.draw.rect(
        ventana, block['color'], (block['x'], block['y'], TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))

# Dibujar jugador


def dibujar_jugador(jugador):
    dibujar_bloque(jugador)
    if jugador['mask']:  # Si tiene mascara, dibuja la mascara
        ventana.blit(jugador['mask'], (jugador['x'], jugador['y']))


# Dibujar enemigos


def dibujar_enemigos(enemigos):
    for enemigo in enemigos:
        dibujar_bloque(enemigo)
        if enemigo['mask']:  # Si tiene mascara, dibuja la mascara
            ventana.blit(enemigo['mask'], (enemigo['x'], enemigo['y']))

# Mover jugador


def mover_jugador(tecla, jugador, vel):
    # Movimiento hacia la izquierda A o <--
    if (tecla[pygame.K_LEFT] or tecla[pygame.K_a]) and jugador['x'] > vel:
        jugador['x'] -= vel
    # Movimiento hacia la derecha D o -->
    if (tecla[pygame.K_RIGHT] or tecla[pygame.K_d]) and jugador['x'] < ANCHO_VENTANA - TAMAÑO_BLOQUE - vel:
        jugador['x'] += vel


# Movimiento de enemigos
def mover_enemigos(enemigos, sentido_movimiento):
    for enemigo in enemigos:
        enemigo['x'] += sentido_movimiento * 1  # velocidad de movimiento
        # controla que llegue a los bordes
        if enemigo['x'] >= ANCHO_VENTANA - TAMAÑO_BLOQUE or enemigo['x'] <= 0:
            for e in enemigos:
                e['y'] += 15  # Descenso de 15 píxeles
            sentido_movimiento *= -1  # Invertir el sentido para el siguiente movimiento en X
            break  # Salir del bucle, solo cambiar una vez el sentido

    return sentido_movimiento


# Dibujar proyectil


def dibujar_proyectil(proyectil):
    # Cambiar el tamaño según sea necesario
    ancho_proyectil = ANCHO_PROYECTIL
    alto_proyectil = ALTO_PROYECTIL
    x_proyectil = proyectil['x'] - ancho_proyectil // 2
    y_proyectil = proyectil['y']
    pygame.draw.rect(
        ventana, proyectil['color'], (x_proyectil, y_proyectil, ancho_proyectil, alto_proyectil))

# Función para dibujar proyectiles


def enemigos_disparan(enemigos, proyectiles):
    for enemigo in enemigos:
        disparos_enemigos(enemigo, proyectiles)


# Función para disparar

# Diparo de proyectiles del jugador


def disparar_proyectil(jugador, proyectiles):
    x = jugador['x'] + TAMAÑO_BLOQUE // 2   # Posicion del proyectil
    y = jugador['y']
    proyectil = crear_proyectil(x, y, jugador['color'])
    if jugador['color'] == COLOR_JUGADOR:
        proyectil['mask'] = ARGENTINA
    proyectiles.append(proyectil)


# Movimiento de los proyextiles

# Jugador


def mover_proyectiles_jugador(proyectiles):
    for proyectil in proyectiles:
        proyectil['y'] -= 5  # Mover proyectil hacia arriba

# Enemigos


def mover_proyectiles_enemigos(proyectiles):
    for proyectil in proyectiles:
        proyectil['y'] += 5  # Mover hacia abajo


# Función para detectar colisiones entre dos rectángulos


def detectar_colision(rect1, rect2):
    return rect1.colliderect(rect2)

# Función para detectar colisiones entre mascaras
