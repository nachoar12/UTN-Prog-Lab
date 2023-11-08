import pygame
import random


# Inicialización de Pygame
pygame.init()
# Inicializacion de la musica de fondo
reproduciendo_musica = True

# Bucle del juego

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


# Inicializar Pygame
pygame.init()
# Inicio de pantalla
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Politic Invaders - Pantalla de Inicio")

# colores
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# tamaño de botones
ancho_boton = 250
alto_boton = 75

# posicion de botones
x_boton = ANCHO_VENTANA // 2 - ancho_boton
y_boton = ALTO_VENTANA // 3 - alto_boton
distancia_boton = 150

# texto posicionamiento
texto_pos_x = ANCHO_VENTANA // 2 - 100
texto_pos_y = ALTO_VENTANA // 2


# Función para crear botones


def dibujar_boton(ventana, color, color_hover, x_boton, y_boton, ancho_boton, alto_boton, texto):
    pos_mouse = pygame.mouse.get_pos()
    btn = pygame.draw.rect(
        ventana, color, (x_boton, y_boton, ancho_boton, alto_boton), border_radius=25)
    if btn.collidepoint(pos_mouse):
        color = color_hover
    pygame.draw.rect(ventana, color, btn, border_radius=25)
    texto_superficie = fuente_juego.render(texto, True, BLANCO)
    x_texto = x_boton + ancho_boton // 2
    y_texto = y_boton + alto_boton // 2
    centro_texto = texto_superficie.get_rect(
        center=(x_texto, y_texto))
    ventana.blit(texto_superficie, centro_texto)
    return btn


x_centro_boton = x_boton + ancho_boton // 2
distancia_texto = 75

# Pantalla configuracion

# Funcion para mostrar texto centrado


def mostrar_texto_centrado(ventana, texto, rect_texto, distancia_texto, color, ):
    # Renderiza el texto con la fuente y el color especificados
    texto_superficie = fuente_instrucciones.render(texto, True, color)
    # Calcula la posición x para centrar el texto
    pos_x = (ventana.get_width() - rect_texto.width) // 2
    # Calcula la posición y para centrar el texto
    pos_y = distancia_texto
    # Muestra el texto en la posición centrada
    ventana.blit(texto_superficie, (pos_x, distancia_texto))


def ventana_instrucciones():
    texto_atras = fuente_game_over.render(
        "ESC = Atras:", True, (BLANCO))
    texto_disclaimer = "DISCLAIMER"
    rect_texto_disclaimer = fuente_instrucciones.render(
        texto_disclaimer, True, (ROJO)).get_rect()
    texto_disclaimer_1 = "Este juego solo tiene fines ludicos y humoristicos,"
    rect_texto_disclaimer_1 = fuente_instrucciones.render(
        texto_disclaimer_1, True, (ROJO)).get_rect()
    texto_disclaimer_2 = "por lo cual no pretende ofender a nigun partidario politico"
    rect_texto_disclaimer_2 = fuente_instrucciones.render(
        texto_disclaimer_2, True, (ROJO)).get_rect()
    texto_instrucciones = "Instrucciones:"
    rect_texto_instrucciones = fuente_instrucciones.render(
        texto_instrucciones, True, (BLANCO)).get_rect()
    texto_instrucciones_1 = "Movimiento: A y D  o  <-  y  ->"
    rect_texto_instrucciones_1 = fuente_instrucciones.render(
        texto_instrucciones_1, True, (BLANCO)).get_rect()
    texto_instrucciones_2 = "Disparo: Barra espacidora o flecha hacia arriba"
    rect_texto_instrucciones_2 = fuente_instrucciones.render(
        texto_instrucciones_2, True, (BLANCO)).get_rect()

    ventana.fill(NEGRO)
    ventana.blit(texto_atras, (50, 50))
    mostrar_texto_centrado(ventana, texto_disclaimer,
                           rect_texto_disclaimer, ALTO_VENTANA // 3 - distancia_texto * 2, ROJO)
    mostrar_texto_centrado(ventana, texto_disclaimer_1,
                           rect_texto_disclaimer_1, ALTO_VENTANA // 3 - distancia_texto, ROJO)
    mostrar_texto_centrado(ventana, texto_disclaimer_2,
                           rect_texto_disclaimer_2, ALTO_VENTANA // 3, ROJO)
    mostrar_texto_centrado(ventana, texto_instrucciones,
                           rect_texto_instrucciones, ALTO_VENTANA // 3 + distancia_boton, BLANCO)
    mostrar_texto_centrado(ventana, texto_instrucciones_1,
                           rect_texto_instrucciones_1, ALTO_VENTANA // 3 + distancia_boton * 2, BLANCO)
    mostrar_texto_centrado(ventana, texto_instrucciones_2,
                           rect_texto_instrucciones_2, ALTO_VENTANA // 3 + distancia_texto * 3, BLANCO)
    pygame.display.update()
    config = True
    while config:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                config = False
                cerrar_juego()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    config = False
                    return


def menu_principal():
    reloj = pygame.time.Clock()
    corriendo = True

    contador_de_clicks = 0
    while corriendo:
        ventana.fill(NEGRO)
        reloj.tick(FPS)
        # Dibujo titulo principal
        btn_titulo_pricipal = dibujar_boton(
            ventana, NEGRO, NEGRO, x_centro_boton, y_boton - distancia_boton, ancho_boton, alto_boton, "* POLITIC INVADERS * ")
        # Dibujar botones con efecto hover
        btn_inicio = dibujar_boton(
            ventana, AZUL, VERDE, x_centro_boton, y_boton, ancho_boton, alto_boton, "Jugar ")
        btn_config = dibujar_boton(
            ventana, AZUL, VERDE, x_centro_boton, y_boton + distancia_boton, ancho_boton, alto_boton, "Instrucciones")
        btn_salir = dibujar_boton(
            ventana, AZUL, VERDE, x_centro_boton, y_boton + distancia_boton * 2, ancho_boton, alto_boton, "Salir")

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                corriendo = False
                cerrar_juego()
            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    cursor = evento.pos

                    if btn_titulo_pricipal.collidepoint(cursor[0], cursor[1]):
                        contador_de_clicks += 1
                        print(f"Clicks : {contador_de_clicks}")
                    if btn_inicio.collidepoint(cursor[0], cursor[1]):
                        print("Iniciando juego...")
                        return
                    elif btn_config.collidepoint(cursor[0], cursor[1]):
                        print("Abriendo instrucciones")
                        ventana_instrucciones()
                    elif btn_salir.collidepoint(cursor[0], cursor[1]):
                        cerrar_juego()
            if contador_de_clicks == 10:
                print("Abriendo ventana de trucos...")
                ventana_de_trucos()

            pygame.display.update()


menu_principal()

# Pausa del juego


def pausar_juego():
    texto_pausa = fuente_game_over.render("Pausa", True, (BLANCO))
    texto_rect = texto_pausa.get_rect()
    texto_rect.center = (ANCHO_VENTANA // 2 - 30, ALTO_VENTANA // 2)
    ventana.blit(texto_pausa, texto_rect)
    pygame.display.update()
    esperar_usuario()
    sonido_pausa.play()


# Pantalla Game Over


def ventana_game_over():
    ventana.fill(NEGRO)
    texto_game_over = fuente_game_over.render("Game Over", True, (BLANCO))
    texto_reiniciar = fuente_game_over.render(
        "Presione R para reiniciar", True, (BLANCO))
    texto_max_score = fuente_game_over.render(
        f"Max Score: ", True, (NARANJA))
    ventana.blit(texto_game_over, (texto_pos_x, texto_pos_y - 150))
    ventana.blit(texto_reiniciar, (texto_pos_x - 75, texto_pos_y))
    ventana.blit(texto_max_score, (texto_pos_x, ALTO_VENTANA - 100))
    pygame.display.update()
    game_over = True
    while game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    game_over = False
                    return


def ventana_de_trucos():
    pass


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


def detectar_colision_mascara(mascara_1, x1, y1, mascara_2, x2, y2):
    offset = (x2 - x1, y2 - y1)
    return mascara_1.overlap(mascara_2, offset)

# Dibujar mascaras


def dibujar_mascara(mascara, x, y, ventana):
    superficie = mascara.to_surface()
    ventana.blit(superficie, (x, y))


def bucle_juego():
    global reproduciendo_musica, sonido_colision, sonido_danio, sonido_game_over_ganar, sonido_pausa, sonido_game_over_perder, sonido_proyectiles
    jugador = crear_jugador()
    enemigos = crear_grilla_enemigos()
    proyectiles_jugador = []  # Lista para los proyectiles del jugador
    proyectiles_enemigos = []  # Lista para los proyectiles de los enemigos

    reloj = pygame.time.Clock()
    corriendo = True
    direccion_movimiento = 1  # Dirección de movimiento inicial - derecha
    vidas_jugador = VIDAS_JUGADOR
    enemigos_eliminados = 0
    # max_score = 0
    pygame.mixer.music.play(1)
    # Bucle menu
    menu_principal()
    # Bucle interno
    while corriendo:
        # print("Juego ejecutándose...")
        reloj.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
                cerrar_juego()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_p:
                sonido_pausa.play()
                pausar_juego()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_m:
                if reproduciendo_musica:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                reproduciendo_musica = not reproduciendo_musica

            if evento.type == pygame.KEYDOWN and (evento.key == pygame.K_SPACE or evento.key == pygame.K_UP):
                disparar_proyectil(jugador, proyectiles_jugador)
                sonido_proyectiles.play()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                corriendo = False
                bucle_juego()

        teclas = pygame.key.get_pressed()
        mover_jugador(teclas, jugador, vel)
        mover_proyectiles_jugador(proyectiles_jugador)
        # Movimiento de proyectiles de enemigos
        mover_proyectiles_enemigos(proyectiles_enemigos)
        # Disparo de proyectiles de enemigos
        enemigos_disparan(enemigos, proyectiles_enemigos)
        direccion_movimiento = mover_enemigos(enemigos, direccion_movimiento)
        # proyectil_jugador_disparados = 0
        # proyectil_enemigos_disparados = 0

        # Proyectiles jugador

        for proyectil_jugador in proyectiles_jugador[:]:
            # proyectil_jugador_disparados += 1
            for enemigo in enemigos[:]:
                if detectar_colision(pygame.Rect(enemigo['x'], enemigo['y'], TAMAÑO_BLOQUE, TAMAÑO_BLOQUE),
                                     pygame.Rect(proyectil_jugador['x'], proyectil_jugador['y'], ANCHO_PROYECTIL, ALTO_PROYECTIL)):
                    try:  # Error el proyectil no se encuentra en la lista
                        proyectiles_jugador.remove(proyectil_jugador)
                    except:
                        pass
                    sonido_colision.play()
                    enemigos.remove(enemigo)
                    enemigos_eliminados += 1

                # sacar el proyectil una vez que sale de la pantalla
                elif len(proyectiles_jugador) > 0 and proyectil_jugador["y"] + ALTO_VENTANA < ALTO_VENTANA - ALTO_PROYECTIL:
                    try:  # Error el proyectil no se encuentra en la lista
                        proyectiles_jugador.remove(proyectil_jugador)
                    except:
                        pass

        # Proyectiles enemigos

        for proyectil_enemigo in proyectiles_enemigos[:]:
            # proyectil_enemigos_disparados += 1

            if detectar_colision(pygame.Rect(jugador['x'], jugador['y'], TAMAÑO_BLOQUE, TAMAÑO_BLOQUE),
                                 pygame.Rect(proyectil_enemigo['x'], proyectil_enemigo['y'], 10, 10)):
                proyectiles_enemigos.remove(proyectil_enemigo)
                sonido_danio.play()
                vidas_jugador -= 1
            # sacar el proyectil una vez que sale de la pantalla
            elif proyectil_enemigo["y"] > ALTO_VENTANA:
                proyectiles_enemigos.remove(proyectil_enemigo)

        # Texto Score, vidas, pausa

        texto_vidas = fuente_juego.render(
            f"Vidas: {vidas_jugador}", True, (BLANCO))
        texto_enemigos_eliminados = fuente_juego.render(
            f"Enemigos eliminados: {enemigos_eliminados}", True, (BLANCO))
        texto_pausa = fuente_juego.render("P = Pausa", True, (BLANCO))
        texto_mute = fuente_juego.render("M = Mute", True, (BLANCO))

        # Game Over 0 vidas
        if vidas_jugador <= 0:
            corriendo = False
            # print("¡Has perdido! Se acabaron las vidas.")
            pygame.mixer.music.pause()
            sonido_game_over_perder.play()
            ventana_game_over()
            print(f"Max Score: {enemigos_eliminados}")
            bucle_juego()

        # Game Over enemigos eliminados
        if enemigos_eliminados == FILA_ENEMIGOS * COLUMNA_ENEMIGOS:
            pygame.mixer.music.pause()
            sonido_game_over_ganar.play()
            ventana_game_over()
            # Agregar enemigos por cada 50 eleminados
            # El jugador elimino a todos los enemigos
            print("¡Has ganado! Todos los enemigos han sido eliminados.")
            print(f"Max Score: {enemigos_eliminados}")
            bucle_juego()

        # Comienzo a dibujar la pantalla
        ventana.fill(NEGRO)

        # dibujar_jugador(jugador)
        dibujar_mascara(mascara_jugador, rect_jugador.x,
                        rect_jugador.y, ventana)
        dibujar_enemigos(enemigos)
        # Dibujar proyectiles del jugador
        dibujar_proyectiles(proyectiles_jugador)
        # Dibujar proyectiles de los enemigos
        dibujar_proyectiles(proyectiles_enemigos)
        # Dibujar Score y vidas
        ventana.blit(texto_vidas, (10, 10))
        ventana.blit(texto_enemigos_eliminados, (ANCHO_VENTANA - 315, 10))
        ventana.blit(texto_pausa, (10, ALTO_VENTANA - 30))
        ventana.blit(texto_mute, (ANCHO_VENTANA - 130, ALTO_VENTANA - 30))

        pygame.display.update()

    cerrar_juego()


bucle_juego()
