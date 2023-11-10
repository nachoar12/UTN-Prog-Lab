import pygame
from config import *

# Funciones

# Función para cerrar el juego


def cerrar_juego():
    """
    Cierra el juego y sale de la aplicación.
    """
    print("Cerrando juego...")
    pygame.quit()
    exit()

# Función para esperar a que el usuario interactúe con el juego


def esperar_usuario():
    """
    Espera a que el usuario interactúe con el juego, como cerrar la ventana o presionar una tecla.
    """
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    cerrar_juego()
                if evento.key == pygame.K_p:
                    return

# Función para crear un jugador


def crear_jugador():
    """
    Crea un jugador con una posición inicial, color y máscara específicos.

    Returns:
    dict: Un diccionario que representa al jugador.
    """
    return {
        'x': ANCHO_VENTANA // 2 - TAMAÑO_BLOQUE // 2,
        'y': ALTO_VENTANA - TAMAÑO_BLOQUE * 1.5,
        'color': COLOR_JUGADOR,
        'mask': CABILDO
    }


# Función para crear un enemigo

def crear_enemigo(x, y, color):
    """
    Crea un enemigo con una posición, color y máscara específicos.

    Args:
    x (int): La coordenada X inicial del enemigo.
    y (int): La coordenada Y inicial del enemigo.
    color (tuple): El color del enemigo en formato (R, G, B).

    Returns:
    dict: Un diccionario que representa al enemigo.
    """
    return {'x': x, 'y': y, 'color': color, 'mask': None, 'mascara': None}
# Función para dibujar un bloque en la pantalla


def dibujar_bloque(block):
    """
    Dibuja un bloque en la ventana del juego. Puede usar una máscara si está definida en el bloque.

    Args:
    block (dict): Un diccionario que representa el bloque a dibujar.
    """
    if block['mask']:  # Si tiene mascara, dibuja la mascara
        ventana.blit(block['mask'], (block['x'], block['y']))
    else:
        pygame.draw.rect(
            ventana, block['color'], (block['x'], block['y'], TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))


# Función para dibujar al jugador en la pantalla


def dibujar_jugador(jugador):
    """
    Dibuja al jugador en la ventana del juego.

    Args:
    jugador (dict): Un diccionario que representa al jugador.
    """
    dibujar_bloque(jugador)


# Función para dibujar enemigos en la pantalla

def dibujar_enemigos(enemigos):
    """
    Dibuja a los enemigos en la ventana del juego.

    Args:
    enemigos (list): Una lista de diccionarios que representan a los enemigos.
    """
    for enemigo in enemigos:
        dibujar_bloque(enemigo)
        if enemigo['mask']:  # Si tiene mascara, dibuja la mascara
            ventana.blit(enemigo['mask'], (enemigo['x'], enemigo['y']))


# Función para crear una matriz de enemigos y asignar máscaras según su color
def crear_grilla_enemigos():
    """
    Crea una matriz de enemigos y asigna máscaras según su color.

    Returns:
    list: Una lista de diccionarios que representan a los enemigos.
    """
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
                enemigo['mascara'] = mascara_massa
            elif enemigo["color"] == (117, 59, 189):  # violeta
                enemigo['mask'] = MILEI
                enemigo['mascara'] = mascara_milei
            elif enemigo["color"] == (254, 221, 0):  # amarillo
                enemigo['mask'] = BULRICH
                enemigo['mascara'] = mascara_bulrich
            elif enemigo["color"] == (67, 72, 143):  # azul
                enemigo['mask'] = SCHIARETTI
                enemigo['mascara'] = mascara_schiaretti
            elif enemigo["color"] == (249, 84, 97):  # rojo
                enemigo['mask'] = BREGMAN
                enemigo['mascara'] = mascara_bregman

            enemigos.append(enemigo)
    return enemigos

# Función para crear un proyectil


def crear_proyectil(x, y, color):
    """
    Crea un proyectil con una posición y color específicos.

    Args:
    x (int): La coordenada X inicial del proyectil.
    y (int): La coordenada Y inicial del proyectil.
    color (tuple): El color del proyectil en formato (R, G, B).

    Returns:
    dict: Un diccionario que representa al proyectil.
    """
    return {'x': x, 'y': y, 'color': color, 'mask': None, 'mascara': None}

# Dibujar proyectiles

# Función para dibujar proyectiles en la pantalla


def dibujar_proyectiles(proyectiles):
    """
    Dibuja los proyectiles en la ventana.

    Args:
    proyectiles (list): Lista de diccionarios que representan los proyectiles con sus propiedades.
    Cada diccionario contiene:
    - 'mask' (surface): Superficie de la máscara asociada al proyectil (opcional, puede ser None).
    - 'x' (int): Posición en el eje x del proyectil.
    - 'y' (int): Posición en el eje y del proyectil.
    - 'color' (tuple): Tupla que representa el color del proyectil (utilizado si no hay máscara).
    """
    ANCHO_PROYECTIL = 10  # Ancho predeterminado de los proyectiles
    ALTO_PROYECTIL = 10  # Alto predeterminado de los proyectiles

    for proyectil in proyectiles:
        if proyectil['mask']:
            # Verifica si hay una máscara asociada al proyectil y la dibuja en la posición x, y.
            ventana.blit(proyectil['mask'], (proyectil['x'], proyectil['y']))
        else:
            # Si no hay máscara, dibuja un rectángulo con el color del proyectil en la posición x, y.
            ancho_proyectil = ANCHO_PROYECTIL
            alto_proyectil = ALTO_PROYECTIL
            # Centra el proyectil en el eje x
            x_proyectil = proyectil['x'] - ancho_proyectil // 2
            y_proyectil = proyectil['y']
            pygame.draw.rect(ventana, proyectil['color'], (
                x_proyectil, y_proyectil, ancho_proyectil, alto_proyectil))


# Función para gestionar los disparos de los enemigos


def disparos_enemigos(enemigo, proyectiles, probabilidad_disparo):
    """
    Genera los disparos de los enemigos asignando las mascaras correspondientes y agrega proyectiles a la lista de proyectiles.

    Args:
    enemigo (dict): Un diccionario que representa al enemigo.
    proyectiles (list): Una lista de diccionarios que representan a los proyectiles.
    """
    # Número aleatorio para simular la probabilidad de disparo
    prob_disparo = random.randint(1, 2000)
    if prob_disparo <= probabilidad_disparo:  # 5% de probabilidad de disparo
        # Ajustar la posición del proyectil
        x = enemigo['x'] + TAMAÑO_BLOQUE // 2
        y = enemigo['y'] + TAMAÑO_BLOQUE
        proyectil = crear_proyectil(x, y, enemigo['color'])
        if enemigo["color"] == (0, 156, 222):  # celeste
            proyectil['mask'] = CHORIPAN
            proyectil['mascara'] = mascara_choripan
        elif enemigo["color"] == (117, 59, 189):  # violeta
            proyectil['mask'] = DOLAR
            proyectil['mascara'] = mascara_dolar
        elif enemigo["color"] == (254, 221, 0):  # amarillo
            proyectil['mask'] = VINO
            proyectil['mascara'] = mascara_vino
        elif enemigo["color"] == (67, 72, 143):  # azul
            proyectil['mask'] = FERNET
            proyectil['mascara'] = mascara_fernet
        elif enemigo["color"] == (249, 84, 97):  # rojo
            proyectil['mask'] = BANDERIN
            proyectil['mascara'] = mascara_banderin
        proyectiles.append(proyectil)


# Momiviento del jugador
# Función para mover al jugador

def mover_jugador(tecla, jugador, vel):
    """
    Mueve al jugador a la izquierda o derecha según las teclas presionadas.

    Args:
    tecla (dict): Un diccionario que contiene las teclas presionadas.
    jugador (dict): Un diccionario que representa al jugador.
    vel (int): La velocidad de movimiento del jugador.
    """
    # Movimiento hacia la izquierda A o <--
    if (tecla[pygame.K_LEFT] or tecla[pygame.K_a]) and jugador['x'] > vel:
        jugador['x'] -= vel
    # Movimiento hacia la derecha D o -->
    if (tecla[pygame.K_RIGHT] or tecla[pygame.K_d]) and jugador['x'] < ANCHO_VENTANA - TAMAÑO_BLOQUE - vel:
        jugador['x'] += vel


# Movimiento de enemigos
# Función para mover a los enemigos en la pantalla

def mover_enemigos(enemigos, sentido_movimiento, velocidad_enemigos):
    """
    Mueve a los enemigos en la pantalla y cambia su dirección si alcanzan los bordes.

    Args:
        enemigos (list): Una lista de diccionarios que representan a los enemigos.
        sentido_movimiento (int): El sentido del movimiento de los enemigos (1 o -1).

    Returns:
        int: El nuevo sentido del movimiento de los enemigos.
    """
    for enemigo in enemigos:
        enemigo['x'] += sentido_movimiento * \
            velocidad_enemigos  # velocidad de movimiento
        # controla que llegue a los bordes
        if enemigo['x'] >= ANCHO_VENTANA - TAMAÑO_BLOQUE or enemigo['x'] <= 0:
            for e in enemigos:
                e['y'] += 15  # Descenso de 15 píxeles
            sentido_movimiento *= -1  # Invertir el sentido para el siguiente movimiento en X
            break  # Salir del bucle, solo cambiar una vez el sentido

    return sentido_movimiento


# Dibujar proyectiles

# Función para dibujar un proyectil en la pantalla
def dibujar_proyectil(proyectil):
    """
    Dibuja un proyectil en la ventana del juego.

    Args:
        proyectil (dict): Un diccionario que representa al proyectil.
    """
    # Cambiar el tamaño según sea necesario
    ancho_proyectil = ANCHO_PROYECTIL
    alto_proyectil = ALTO_PROYECTIL
    x_proyectil = proyectil['x'] - ancho_proyectil // 2
    y_proyectil = proyectil['y']
    pygame.draw.rect(
        ventana, proyectil['color'], (x_proyectil, y_proyectil, ancho_proyectil, alto_proyectil))

# Función para que los enemigos disparen proyectiles


def enemigos_disparan(enemigos, proyectiles, probabilidad_disparo):
    """
    Genera los disparos de proyectiles enemigos y los agrega a la lista de proyectiles.

    Args:
        enemigos (list): Una lista de diccionarios que representan a los enemigos.
        proyectiles (list): Una lista de diccionarios que representan a los proyectiles.
    """
    for enemigo in enemigos:
        disparos_enemigos(enemigo, proyectiles, probabilidad_disparo)


# Función para disparar

# Función para que el jugador dispare un proyectil


def disparar_proyectil(jugador, proyectiles):
    """
    Permite al jugador disparar un proyectil y lo agrega a la lista de proyectiles.

    Args:
        jugador (dict): Un diccionario que representa al jugador.
        proyectiles (list): Una lista de diccionarios que representan a los proyectiles.
    """
    x = jugador['x'] + TAMAÑO_BLOQUE // 2 - \
        ANCHO_PROYECTIL // 2   # Posicion del proyectil
    y = jugador['y']
    proyectil = crear_proyectil(x, y, jugador['color'])
    if jugador['color'] == COLOR_JUGADOR:
        proyectil['mask'] = ARGENTINA
    else:
        x = jugador['x'] + TAMAÑO_BLOQUE // 2  # Posicion del proyectil
    proyectiles.append(proyectil)


# Movimiento de los proyectiles

# Jugador
# Función para mover los proyectiles del jugador

def mover_proyectiles_jugador(proyectiles):
    """
    Mueve los proyectiles disparados por el jugador hacia arriba.

    Args:
        proyectiles (list): Una lista de diccionarios que representan a los proyectiles.
    """
    for proyectil in proyectiles:
        proyectil['y'] -= 5  # Mover proyectil hacia arriba

# Enemigos
# Función para mover los proyectiles de los enemigos


def mover_proyectiles_enemigos(proyectiles):
    """
    Mueve los proyectiles disparados por los enemigos hacia abajo.

    Args:
        proyectiles (list): Una lista de diccionarios que representan a los proyectiles.
    """
    for proyectil in proyectiles:
        proyectil['y'] += 5  # Mover hacia abajo


# Colisiones
# Función para detectar colisiones entre dos rectángulos


# def detectar_colision(rect1, rect2):
#     """
#     Detecta la colisión entre dos rectángulos.

#     Args:
#         rect1 (pygame.Rect): El primer rectángulo a comparar.
#         rect2 (pygame.Rect): El segundo rectángulo a comparar.

#     Returns:
#         bool: True si hay colisión, False en caso contrario.
#     """
#     return rect1.colliderect(rect2)


# Score
# Función para obtener el maximo score almacenado


def obtener_highscore(score):
    """
    Obtiene el puntaje más alto (highscore) proporcionado.

    Args:
        score (int or float): El puntaje que se desea verificar.

    Returns:
        int : El mismo puntaje que se ingresó, ya que devuelve el puntaje proporcionado.
    """
    return score
