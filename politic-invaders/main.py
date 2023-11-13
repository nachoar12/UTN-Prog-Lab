import pygame
from config import *
from ventanas import *
from funciones import *


# Inicialización de Pygame
pygame.init()
# Inicializacion de la musica de fondo
reproduciendo_musica = True

# Bucle del juego


def bucle_juego():
    global reproduciendo_musica
    pygame.mixer.music.play(-1)
    jugador = crear_jugador()
    enemigos = crear_grilla_enemigos()
    vida_extra = crear_vida_extra()
    if vida_extra["x"] == jugador["x"]:
        vida_extra = crear_vida_extra()
    vidas_extras = []
    proyectiles_jugador = []  # Lista para los proyectiles del jugador
    proyectiles_enemigos = []  # Lista para los proyectiles de los enemigos
    reloj = pygame.time.Clock()
    corriendo = True
    direccion_movimiento_enemigo = 1  # Dirección de movimiento inicial - derecha
    vidas_jugador = VIDAS_JUGADOR
    vel_enemigos = velocidad_enemigos
    prob_disparo_enemigo = probabilidad_disparo_enemigo
    highscore = obtener_highscore(max_score)
    # print(highscore)

    score = 0
    enemigos_eliminados = 0

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
                menu_principal()
                bucle_juego()

        teclas = pygame.key.get_pressed()
        mover_jugador(teclas, jugador, velocidad_jugador)
        mover_proyectiles_jugador(proyectiles_jugador)
        # Movimiento de proyectiles de enemigos
        mover_proyectiles_enemigos(proyectiles_enemigos)
        # Disparo de proyectiles de enemigos
        enemigos_disparan(enemigos, proyectiles_enemigos, prob_disparo_enemigo)
        direccion_movimiento_enemigo = mover_enemigos(
            enemigos, direccion_movimiento_enemigo, vel_enemigos)
        # proyectil_jugador_disparados = 0
        # proyectil_enemigos_disparados = 0

        # Proyectiles jugador

        for proyectil_jugador in proyectiles_jugador[:]:
            # proyectil_jugador_disparados += 1
            for enemigo in enemigos[:]:
                offset = (enemigo['x'] - proyectil_jugador['x'],
                          enemigo['y'] - proyectil_jugador['y'])
                if mascara_proyectil_jugador.overlap(enemigo['mascara'], offset) != None:
                    if proyectil_jugador in proyectiles_jugador:  # Error el proyectil no se encuentra en la lista
                        proyectiles_jugador.remove(proyectil_jugador)
                    sonido_colision.play()
                    enemigos.remove(enemigo)
                    enemigos_eliminados += 1
                    score += 1
                # sacar el proyectil una vez que sale de la pantalla
                if proyectil_jugador in proyectiles_jugador and proyectil_jugador["y"] + ALTO_VENTANA < ALTO_VENTANA - ALTO_PROYECTIL:
                    proyectiles_jugador.remove(proyectil_jugador)

        # Proyectiles enemigos

        for proyectil_enemigo in proyectiles_enemigos[:]:
            # proyectil_enemigos_disparados += 1
            offset = (jugador['x'] - proyectil_enemigo['x'],
                      jugador['y'] - proyectil_enemigo['y'])
            if proyectil_enemigo['mascara'].overlap(mascara_jugador, offset) != None:
                proyectiles_enemigos.remove(proyectil_enemigo)
                sonido_danio.play()
                vidas_jugador -= 1
            # sacar el proyectil una vez que sale de la pantalla
            elif proyectil_enemigo["y"] > ALTO_VENTANA:
                proyectiles_enemigos.remove(proyectil_enemigo)

        for vida in vidas_extras[:]:
            offset = (jugador['x'] - vida_extra['x'],
                      jugador['y'] - vida_extra['y'])
            if mascara_vida.overlap(mascara_jugador, offset) != None:
                sonida_vida.play()
                vidas_jugador += 1
                vidas_extras.remove(vida)
        # Texto Score, vidas, pausa

        texto_vidas = fuente_juego.render(
            f"Vidas: {vidas_jugador}", True, (BLANCO))
        texto_puntaje = fuente_juego.render(
            f"Puntaje: {score}", True, (BLANCO))
        texto_pausa = fuente_juego.render("P = Pausa", True, (BLANCO))
        texto_mute = fuente_juego.render("M = Mute", True, (BLANCO))

        # Game Over 0 vidas
        if vidas_jugador <= 0:
            corriendo = False
            # print("¡Has perdido! Se acabaron las vidas.")
            pygame.mixer.music.pause()
            sonido_game_over_perder.play()
            # Guardo el maximo score
            print(f"Score: {score}")
            if score > highscore:
                highscore = score
            ventana_game_over(score)
            bucle_juego()

        # Cada 50 enemigos eliminados
        if enemigos_eliminados == FILA_ENEMIGOS * COLUMNA_ENEMIGOS:
            if vida_extra["x"] == jugador["x"]:
                vida_extra = crear_vida_extra()
            vidas_extras.append(vida_extra)
            enemigos_eliminados = 0  # Reseteo para volver a contar enemigos
            enemigos = crear_grilla_enemigos()  # Vuelvo a crear enemigos
            # Reseteo el movimiento para que vuelvan a la posicion inicial
            direccion_movimiento_enemigo = 1
            vel_enemigos += 0.5  # Aumento la velocidad de los enemigos
            prob_disparo_enemigo += 2  # Aumento la probabilidad de disparo

        if score == 500:
            corriendo = False
            pygame.mixer.music.pause()
            sonido_game_over_ganar.play()
            highscore = score
            print("Has Ganado")
            ventana_win(highscore)
            menu_principal()
            bucle_juego()

        # Comienzo a dibujar la pantalla

        # rectangulo para cargar fondo
        fondo = pygame.Rect(0, 0, ANCHO_VENTANA, ALTO_VENTANA)
        ventana.blit(imagen_bkg, fondo)
        if vidas_extras:
            dibujar_vidas(vidas_extras)
        dibujar_jugador(jugador)
        dibujar_enemigos(enemigos)
        # Dibujar proyectiles del jugador
        dibujar_proyectiles(proyectiles_jugador)
        # Dibujar proyectiles de los enemigos
        dibujar_proyectiles(proyectiles_enemigos)
        # Dibujar Score y vidas
        ventana.blit(texto_vidas, (10, 10))
        ventana.blit(texto_puntaje, (ANCHO_VENTANA - 175, 10))
        ventana.blit(texto_pausa, (10, ALTO_VENTANA - 30))
        ventana.blit(texto_mute, (ANCHO_VENTANA - 130, ALTO_VENTANA - 30))

        pygame.display.update()

    cerrar_juego()


bucle_juego()
# Bucle menu
menu_principal()
bucle_juego()
