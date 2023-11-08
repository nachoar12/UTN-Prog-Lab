import pygame
from config import ALTO_VENTANA, ANCHO_VENTANA, NEGRO, BLANCO, NARANJA, fuente_juego, FPS, fuente_game_over, fuente_instrucciones, sonido_pausa
from funciones import cerrar_juego, esperar_usuario
import json

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
    with open("politic-invaders/scores.json", "r") as scores:
        score = json.load(scores)
        print(scores)
        texto_max_score = fuente_game_over.render(
        f"Score: {score}", True, (NARANJA))
        ventana.blit(texto_max_score, (texto_pos_x, ALTO_VENTANA - 100))

    ventana.blit(texto_game_over, (texto_pos_x, texto_pos_y - 150))
    ventana.blit(texto_reiniciar, (texto_pos_x - 75, texto_pos_y))
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
