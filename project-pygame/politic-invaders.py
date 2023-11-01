import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana del juego
ANCHO_VENTANA, ALTO_VENTANA = 1000, 800
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Politic Invaders")

# Colores
COLORES_ENEMIGOS = [
    (0, 156, 222),  # celeste
    (117, 59, 189),  # violeta
    (254, 221, 0),  # amarillo
    (67, 72, 143),  # azul
    (249, 84, 97)  # rojo
]


COLOR_JUGADOR = (60, 179, 113)

# Tamaño de los bloques
TAMAÑO_BLOQUE = 50
FILA_ENEMIGOS = 5
COLUMNA_ENEMIGOS = 10
DISTANCIA_ENTRE_ENEMIGOS = 25

# Crear jugador


def crear_jugador():
    return {
        'x': ANCHO_VENTANA // 2 - TAMAÑO_BLOQUE // 2,
        'y': ALTO_VENTANA - TAMAÑO_BLOQUE * 2,
        'color': COLOR_JUGADOR
    }

# Crear enemigos según el color


def crear_enemigo(x, y, color):
    return {'x': x, 'y': y, 'color': color}

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
            enemigos.append(enemigo)
    return enemigos

# Dibujar enemigos


def dibujar_enemigos(enemigos):
    for enemigo in enemigos:
        dibujar_bloque(enemigo)

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
    return {'x': x, 'y': y, 'color': color}

# Dibujar proyectil


def dibujar_proyectil(proyectil):
    # Cambiar el tamaño según sea necesario
    ancho_proyectil = 10
    alto_proyectil = 30
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


def dibujar_proyectiles(proyectiles):
    for proyectil in proyectiles:
        dibujar_proyectil(proyectil)

# Crear función para disparo de enemigos de manera aleatoria


def disparar_enemigo(enemigo, proyectiles):
    # Generar un número aleatorio para simular la probabilidad de disparo
    probabilidad_disparo = random.randint(1, 2500)
    if probabilidad_disparo <= 5:  # Por ejemplo, 5% de probabilidad de disparo
        x = enemigo['x'] + TAMAÑO_BLOQUE // 2 - \
            5  # Ajustar la posición del proyectil
        y = enemigo['y'] + TAMAÑO_BLOQUE
        proyectil = crear_proyectil(x, y, enemigo['color'])
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


# Loop del juego
def game_loop():
    jugador = crear_jugador()
    enemigos = crear_grilla_enemigos()
    proyectiles_jugador = []  # Lista para los proyectiles del jugador
    proyectiles_enemigos = []  # Lista para los proyectiles de los enemigos

    vel = 5
    clock = pygame.time.Clock()
    corriendo = True
    sentido_movimiento = 1  # Dirección de movimiento inicial
    vidas_jugador = VIDAS_JUGADOR
    enemigos_eliminados = 0

    # Inside the game loop

    while corriendo:
        # Añade este mensaje para verificar la ejecución del bucle
        print("Bucle del juego ejecutándose...")
        clock.tick(60)
        ventana.fill((0, 0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                disparar_proyectil(jugador, proyectiles_jugador)

        teclas = pygame.key.get_pressed()
        mover_jugador(teclas, jugador, vel)
        mover_proyectiles_jugador(proyectiles_jugador)
        # Movimiento de proyectiles de enemigos
        mover_proyectiles_enemigos(proyectiles_enemigos)
        # Disparo de proyectiles de enemigos
        enemigos_disparan(enemigos, proyectiles_enemigos)

        for proyectil_jugador in proyectiles_jugador[:]:
            for enemigo in enemigos[:]:
                if detectar_colision(pygame.Rect(enemigo['x'], enemigo['y'], TAMAÑO_BLOQUE, TAMAÑO_BLOQUE),
                                     pygame.Rect(proyectil_jugador['x'], proyectil_jugador['y'], 10, 10)):
                    proyectiles_jugador.remove(proyectil_jugador)
                    enemigos.remove(enemigo)
                    enemigos_eliminados += 1

        for proyectil_enemigo in proyectiles_enemigos[:]:
            if detectar_colision(pygame.Rect(jugador['x'], jugador['y'], TAMAÑO_BLOQUE, TAMAÑO_BLOQUE),
                                 pygame.Rect(proyectil_enemigo['x'], proyectil_enemigo['y'], 10, 10)):
                proyectiles_enemigos.remove(proyectil_enemigo)
                vidas_jugador = actualizar_vidas_jugador(vidas_jugador)

        # Texto Score y vidas
        texto_vidas = fuente.render(
            f"Vidas: {vidas_jugador}", True, (255, 255, 255))
        texto_enemigos_eliminados = fuente.render(
            f"Enemigos eliminados: {enemigos_eliminados}", True, (255, 255, 255))

        if vidas_jugador <= 0:
            # El jugador perdió, se detiene el juego
            corriendo = False
            print("¡Has perdido! Se acabaron las vidas.")
            ventana_game_over()
            reiniciar = True
            while reiniciar:
                for evento in pygame.event.get():
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:
                            reiniciar = False

        if enemigos_eliminados == FILA_ENEMIGOS * COLUMNA_ENEMIGOS:
            # El jugador ha eliminado todos los enemigos
            corriendo = False
            print("¡Has ganado! Todos los enemigos han sido eliminados.")

        sentido_movimiento = mover_enemigos(enemigos, sentido_movimiento)

        dibujar_bloque(jugador)
        dibujar_enemigos(enemigos)
        # Dibujar proyectiles del jugador
        dibujar_proyectiles(proyectiles_jugador)
        # Dibujar proyectiles de los enemigos
        dibujar_proyectiles(proyectiles_enemigos)
        # Dibujar Score y vidas
        ventana.blit(texto_vidas, (10, 10))
        ventana.blit(texto_enemigos_eliminados, (ANCHO_VENTANA - 260, 10))

        pygame.display.update()

    pygame.quit()


game_loop()
