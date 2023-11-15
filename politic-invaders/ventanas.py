import pygame
from config import ALTO_VENTANA, ANCHO_VENTANA, NEGRO, BLANCO, NARANJA, ROJO, VERDE, AZUL, CELESTE, AMARILLO, fuente_juego, FPS, fuente_game_over, fuente_instrucciones, sonido_pausa, menu_bkg, instrucciones_bkg, game_over_bkg, game_over_win_bkg
from funciones import cerrar_juego, esperar_usuario, cargar_score


# Inicialización de Pygame
pygame.init()

# Inicio de la pantalla y configuración
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))


# Tamaño y posición de botones
ancho_boton = 250
alto_boton = 75
x_boton = ANCHO_VENTANA // 2 - ancho_boton
y_boton = ALTO_VENTANA // 3 - alto_boton
distancia_boton = 150

# Posicionamiento del texto
texto_pos_x = ANCHO_VENTANA // 2 - 100
texto_pos_y = ALTO_VENTANA // 2


# Función para crear botones


def dibujar_boton(ventana, color, color_hover, x_boton, y_boton, ancho_boton, alto_boton, texto):
    """
    Dibuja un botón en la ventana de Pygame.

    Args:
        ventana (Surface): La superficie de la ventana de Pygame.
        color (tuple): Color base del botón.
        color_hover (tuple): Color cuando el cursor está sobre el botón.
        x_boton (int): Coordenada x del botón.
        y_boton (int): Coordenada y del botón.
        ancho_boton (int): Ancho del botón.
        alto_boton (int): Altura del botón.
        texto (str): Texto que se mostrará en el botón.

    Retorna:
        pygame.Rect: Un rectángulo que representa el área del botón.

    Esta función dibuja un botón en la ventana de Pygame con el texto proporcionado. 
    Comprueba si el cursor del mouse está sobre el botón para cambiar el color.
    Devuelve un objeto Rect de Pygame que representa el área del botón creado.
    """
    pos_mouse = pygame.mouse.get_pos()
    btn = pygame.draw.rect(
        ventana, color, (x_boton, y_boton, ancho_boton, alto_boton), border_radius=25)
    if btn.collidepoint(pos_mouse):
        color = color_hover
    pygame.draw.rect(ventana, color, btn, border_radius=25)
    texto_superficie = fuente_juego.render(texto, True, NEGRO)
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
    """
    Muestra texto centrado en la ventana de Pygame.

    Args:
        ventana (Surface): La superficie de la ventana de Pygame.
        texto (str): Texto a mostrar.
        rect_texto (Rect): Rectángulo que representa el área del texto.
        distancia_texto (int): Distancia en el eje Y para centrar el texto.
        color (tuple): Color del texto a mostrar.

    Esta función renderiza el texto en la ventana de Pygame, centrado tanto horizontal como verticalmente.
    """
    texto_superficie = fuente_instrucciones.render(texto, True, color)
    pos_x = (ventana.get_width() - rect_texto.width) // 2
    pos_y = distancia_texto
    ventana.blit(texto_superficie, (pos_x, distancia_texto))


def ventana_instrucciones():
    """
    Muestra la pantalla de instrucciones del juego con texto, un disclaimer y una opcion para salir.

    """
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

    fondo = pygame.Rect(0, 0, ANCHO_VENTANA, ALTO_VENTANA)
    ventana.blit(instrucciones_bkg, fondo)
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
    """
    Función que maneja el menú principal del juego.

    Esta función maneja la pantalla de menú principal del juego. Muestra botones para jugar, ver las instrucciones y salir del juego. Detecta eventos de clics y teclas para permitir al usuario interactuar con el menú.
    """
    reloj = pygame.time.Clock()
    corriendo = True
    contador_de_clicks = 0

    while corriendo:
        fondo = pygame.Rect(0, 0, ANCHO_VENTANA, ALTO_VENTANA)
        ventana.blit(menu_bkg, fondo)
        reloj.tick(FPS)
        # Dibujo título principal
        texto_titulo = "*POLITIC INVADERS*"
        rect_texto_titulo = fuente_instrucciones.render(
            texto_titulo, True, (ROJO)).get_rect()
        mostrar_texto_centrado(ventana, texto_titulo,
                               rect_texto_titulo, ALTO_VENTANA // 3 - distancia_texto * 2.5, BLANCO)
        # Dibujar botones con efecto hover
        btn_inicio = dibujar_boton(
            ventana, CELESTE, BLANCO, x_centro_boton, y_boton, ancho_boton, alto_boton, "Jugar ")
        btn_config = dibujar_boton(
            ventana, BLANCO, AMARILLO, x_centro_boton, y_boton + distancia_boton, ancho_boton, alto_boton, "Instrucciones")
        btn_salir = dibujar_boton(
            ventana, CELESTE, BLANCO, x_centro_boton, y_boton + distancia_boton * 2, ancho_boton, alto_boton, "Salir")

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                corriendo = False
                cerrar_juego()
            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    cursor = evento.pos

                    if btn_inicio.collidepoint(cursor):
                        print("Iniciando juego...")
                        return
                    elif btn_config.collidepoint(cursor):
                        print("Abriendo instrucciones")
                        ventana_instrucciones()
                    elif btn_salir.collidepoint(cursor):
                        cerrar_juego()
            if contador_de_clicks == 10:
                print("Abriendo ventana de trucos...")
                # ventana_de_trucos()

            pygame.display.update()


menu_principal()


# Pausa del juego


def pausar_juego():
    """
    Pausa la ejecución del juego y muestra un mensaje de pausa en la pantalla.

    Esta función pausa el juego y muestra un mensaje de pausa en el centro de la ventana del juego. Se espera a que el usuario responda, luego se reproduce un sonido de pausa para notificar la continuación del juego.
    """
    texto_salir = fuente_game_over.render(
        "*ESC = Salir*", True, (BLANCO))
    ventana.blit(texto_salir, (ANCHO_VENTANA // 2 - 100, 50))
    texto_pausa = fuente_game_over.render("Pausa", True, (BLANCO))
    texto_rect = texto_pausa.get_rect()
    texto_rect.center = (ANCHO_VENTANA // 2 - 30, ALTO_VENTANA // 2)
    ventana.blit(texto_pausa, texto_rect)
    pygame.display.update()
    esperar_usuario()  # Función que espera la interacción del usuario
    sonido_pausa.play()  # Reproducir sonido de pausa


# Pantalla Game Over


def ventana_game_over(score):
    """
    Muestra la pantalla de Game Over.

    Args: 
        score (int): El puntaje a mostrar en la pantalla

    Esta función muestra la pantalla de Game Over, que incluye el puntaje obtenido y un mensaje para reiniciar el juego al presionar la tecla 'R'. El puntaje se recupera desde un archivo txt. Espera a que el usuario presione 'R' para reiniciar el juego.
    """

    highscore = cargar_score()
    fondo = pygame.Rect(0, 0, ANCHO_VENTANA, ALTO_VENTANA)
    ventana.blit(game_over_bkg, fondo)
    texto_reiniciar = fuente_game_over.render(
        "Presione R para reiniciar", True, (BLANCO))
    texto_score = fuente_game_over.render(
        f"Score: {score}", True, (NARANJA))
    texto_highscore = fuente_game_over.render(
        f"Highscore: {highscore}", True, (NARANJA))
    ventana.blit(texto_reiniciar, (texto_pos_x - 75, ALTO_VENTANA - 50))
    ventana.blit(texto_score, (texto_pos_x - 250,  40))
    ventana.blit(texto_highscore, (texto_pos_x + 270,  40))

    pygame.display.update()
    game_over = True
    while game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    cerrar_juego()
                if evento.key == pygame.K_r:
                    game_over = False
                    return


def ventana_win(score):
    """
    Muestra la pantalla de Game Over cuando el jugador gana, es decir cuando llega a 500 puntos.

    Args: 
        score (int): El puntaje a mostrar en la pantalla

    Esta función muestra la pantalla de Game Over, que incluye el puntaje obtenido y un mensaje para reiniciar el juego al presionar la tecla 'R'. El puntaje se recupera desde un archivo txt. Espera a que el usuario presione 'R' para reiniciar el juego.
    """
    highscore = cargar_score()
    ventana.fill(BLANCO)
    fondo = pygame.Rect(0, 0, ANCHO_VENTANA, ALTO_VENTANA)
    ventana.blit(game_over_win_bkg, fondo)
    texto_reiniciar = fuente_game_over.render(
        "Presione R para reiniciar", True, (NEGRO))
    texto_score = fuente_game_over.render(
        f"Score: {score}", True, (NARANJA))
    texto_highscore = fuente_game_over.render(
        f"Highscore: {highscore}", True, (NARANJA))
    ventana.blit(texto_reiniciar, (texto_pos_x - 60, ALTO_VENTANA - 50))
    ventana.blit(texto_score, (texto_pos_x - 250,  40))
    ventana.blit(texto_highscore, (texto_pos_x + 270,  40))

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
