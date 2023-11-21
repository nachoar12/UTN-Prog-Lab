import pygame
import random
from config import *

# Funciones

# Función para cerrar el juego


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
        'y': ALTO_VENTANA - TAMAÑO_BLOQUE * 1.7,
        'color': COLOR_JUGADOR,
        'mask': JUGADOR
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
def cargar_score():
    """
    Carga el puntaje máximo desde un archivo de texto.

    Intenta leer el puntaje máximo desde el archivo 'highscore.txt' ubicado en el directorio 'politic-invaders'.
    Si el archivo existe y contiene un puntaje válido, lo lee y lo devuelve como un número entero.
    Si el archivo no existe o el puntaje no es válido, devuelve un puntaje máximo predeterminado de 0.

    Returns:
    int: El puntaje máximo leído desde el archivo o 0 si no se pudo cargar correctamente.
    """
    try:
        with open("politic-invaders/highscore.txt", "r") as highscore_data:
            # Lee la primera línea y elimina espacios en blanco
            max_score = highscore_data.readline().strip()
            if not max_score:  # Verifica si max_score está vacío después de eliminar espacios en blanco
                max_score = 0
            else:
                # Convierte a entero si no está vacío
                max_score = int(max_score)
    except FileNotFoundError:
        max_score = 0  # Si el archivo no existe, asigna un valor predeterminado de 0
    except (ValueError, TypeError) as error:
        print("Error al cargar el puntaje máximo:", error)
        max_score = 0  # Si hay un error al convertir a entero, asigna un valor predeterminado de 0

    return max_score

# Función para agregar una vida


def crear_vida_extra():
    """
    Crea una vida extra en la posición inicial, color y máscara específicos.

    Returns:
    dict: Un diccionario que representa a la vida.
    """
    return {
        'x': random.randrange(ANCHO_VENTANA // 2 - TAMAÑO_BLOQUE // 2),
        'y': ALTO_VENTANA - TAMAÑO_BLOQUE * 1.2,
        'color': ROJO,
        'mask': VIDA
    }


def dibujar_power_up(power_ups):
    """
    Dibuja las vidas extras en la ventana.

    Args:
    vidas_extras (list): Lista de diccionarios que representan las vidas con sus propiedades.
    Cada diccionario contiene:
    - 'mask' (surface): Superficie de la máscara asociada a la vida (opcional, puede ser None).
    - 'x' (int): Posición en el eje x del proyectil.
    - 'y' (int): Posición en el eje y del proyectil.
    - 'color' (tuple): Tupla que representa el color del proyectil (utilizado si no hay máscara).
    """

    for power_up in power_ups:
        if power_up['mask']:
            # Verifica si hay una máscara asociada al proyectil y la dibuja en la posición x, y.
            ventana.blit(power_up['mask'], (power_up['x'], power_up['y']))
        else:
            # Si no hay máscara, dibuja un rectángulo con el color del proyectil en la posición x, y.
            ancho_power_up = TAMAÑO_BLOQUE // 1.5
            alto_power_up = TAMAÑO_BLOQUE // 1.5
            # Centra el proyectil en el eje x
            x_power_up = power_up['x'] - ancho_power_up // 1.5
            y_power_up = power_up['y']
            pygame.draw.rect(ventana, power_up['color'], (
                x_power_up, y_power_up, ancho_power_up, alto_power_up))


# POSICION Y MASCARA MOTOSIERRA
pos_moto_x = random.randrange(0, ANCHO_VENTANA - TAMAÑO_BLOQUE * 2)
pos_moto_y = 0 - TAMAÑO_BLOQUE
mask_moto = MOTOSIERRA
# POSICION Y MASCARA MOTOSIERRA POWER
pos_moto_power_x = 0 - ANCHO_VENTANA // 2
pos_moto_power_y = 0
mask_moto_power = MOTOSIERRA_POWER


def crear_motosierra(pos_x, pos_y, mask):
    """
    Crea el power up de motosierra en una posición específica, con un color y máscara dados.

    Args:
    pos_x (int): Coordenada x inicial para la posición del power up.
    pos_y (int): Coordenada y inicial para la posición del power up.
    mask (objeto): La máscara específica para el power up de motosierra.

    Returns:
    dict: Un diccionario que representa al power up de motosierra con las siguientes propiedades:
        - 'x': Coordenada x del power up.
        - 'y': Coordenada y del power up.
        - 'color': Color del power up.
        - 'mask': Máscara utilizada para el power up de motosierra.
    """
    return {
        'x': pos_x,
        'y': pos_y,
        'color': BLANCO,
        'mask': mask,
    }


def mover_power_up(power_up):
    """
    Mueve los / el power up hacia abajo.

    Args:
        power_up (list): Una lista de diccionarios que representan a los power up, en este caso la motosierra.
    """
    for power in power_up:
        power["y"] += 5  # Mover power_up hacia abajo


def dibujar_motosierra(motosierra):
    """
    Dibuja un bloque en la ventana del juego. Puede usar una máscara si está definida en el bloque.

    Args:
    block (dict): Un diccionario que representa el bloque a dibujar.
    """
    if motosierra['mask']:  # Si tiene mascara, dibuja la mascara
        ventana.blit(motosierra['mask'], (motosierra['x'], motosierra['y']))
    else:
        pygame.draw.rect(
            ventana, motosierra['color'], (motosierra['x'], motosierra['y'], TAMAÑO_BLOQUE, TAMAÑO_BLOQUE))


def mover_motosierra(motosierras):
    """
    Mueve las motosierras disparadas por el jugador hacia la derecha.

    Args:
        motosierras (list): Una lista de diccionarios que representan al power up motosierra.
    """
    for motosierra in motosierras:
        motosierra["x"] += 3.5


def crear_peron():
    """
    Crea a peron en la posición inicial, color y máscara específicos.

    Returns:
    dict: Un diccionario que representa a peron.
    """
    return {
        'x': ANCHO_VENTANA + TAMAÑO_BLOQUE * 2.5,
        'y': ALTO_VENTANA - TAMAÑO_BLOQUE * 2.5,
        'color': ROJO,
        'mask': PERON
    }


def mover_toasty(toasty, sentido_mov):
    """
    Mueve a los enemigos en la pantalla y cambia su dirección si alcanzan los bordes.

    Args:
        enemigos (list): Una lista de diccionarios que representan a los enemigos.
        sentido_movimiento (int): El sentido del movimiento de los enemigos (1 o -1).

    Returns:
        int: El nuevo sentido del movimiento de los enemigos.
    """

    toasty['x'] += sentido_mov * 6  # velocidad de movimiento
    # controla que llegue a los bordes
    if toasty['x'] <= ANCHO_VENTANA - TAMAÑO_BLOQUE * 3:
        sentido_mov *= -1  # Invertir el sentido para el siguiente movimiento en X

    return sentido_mov


# Funcion para guardar score

def guardar_score(score):
    """
    Guarda el puntaje máximo en un archivo de texto.

    Intenta guardar el puntaje máximo proporcionado en el archivo 'highscore.txt' ubicado en el directorio 'politic-invaders'.

    Args:
    score (int): El puntaje máximo que se desea guardar en el archivo.

    """
    try:
        with open("politic-invaders/highscore.txt", "w") as highscore_data:
            highscore_data.write(str(score))
    except IOError as io_error:
        print("Error al guardar el puntaje máximo:", io_error)
