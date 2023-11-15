import pygame
from config import *
from ventanas import *
from funciones import *


# Inicialización de Pygame
pygame.init()
# Inicializacion de la musica de fondo


# Bucle del juego


def bucle_juego():
    print("Inicia game loop")
    motosierra_on = False
    motosierra_cargada = False
    mover_sierra = False
    toasty = False
    reproduciendo_musica = True
    pygame.mixer.music.play(-1)
    jugador = crear_jugador()
    enemigos = crear_grilla_enemigos()
    vida_extra = crear_vida_extra()
    if vida_extra["x"] == jugador["x"]:
        vida_extra = crear_vida_extra()
    vidas_extras = []
    motosierra = crear_motorosierra(pos_moto_x, pos_moto_y, mask_moto)
    motosierra_power = crear_motorosierra(
        pos_moto_power_x, pos_moto_power_y, mask_moto_power)
    peron = crear_peron()
    poder = 0
    power_up = []
    proyectil_motosierra = []
    proyectiles_jugador = []  # Lista para los proyectiles del jugador
    proyectiles_enemigos = []  # Lista para los proyectiles de los enemigos
    reloj = pygame.time.Clock()
    corriendo = True
    direccion_movimiento_enemigo = 1  # Dirección de movimiento inicial - derecha
    dir_mov_toasty = -1
    vidas_jugador = VIDAS_JUGADOR
    vel_enemigos = velocidad_enemigos
    prob_disparo_enemigo = probabilidad_disparo_enemigo
    highscore = cargar_score()
    # print(highscore)

    score = 0
    enemigos_eliminados = 0
    massa_eliminado = 0
    milei_eliminado = 0
    bulrich_eliminada = 0
    schiaretti_eliminado = 0
    bregman_eliminada = 0
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
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_f:
                if proyectil_motosierra:
                    mover_sierra = True
                    poder -= 1
                    sonido_motosierra.play()
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
        mover_power_up(power_up)
        if mover_sierra:
            mover_motosierra(proyectil_motosierra)
        if toasty:
            dir_mov_toasty = mover_toasty(peron, dir_mov_toasty)
        # proyectil_jugador_disparados = 0
        # proyectil_enemigos_disparados = 0

        # Proyectiles jugador

        for proyectil_jugador in proyectiles_jugador[:]:
            # proyectil_jugador_disparados += 1
            for enemigo in enemigos[:]:
                offset = (enemigo['x'] - proyectil_jugador['x'],
                          enemigo['y'] - proyectil_jugador['y'])
                # Colisión proyecil con enemigo
                if mascara_proyectil_jugador.overlap(enemigo['mascara'], offset) != None:
                    if proyectil_jugador in proyectiles_jugador:  # Error el proyectil no se encuentra en la lista
                        proyectiles_jugador.remove(proyectil_jugador)
                    sonido_colision.play()
                    if enemigo["mask"] == MASSA:
                        massa_eliminado += 1
                        if massa_eliminado == 10:
                            sonido_massa.play()
                    elif enemigo["mask"] == MILEI:
                        milei_eliminado += 1
                        if milei_eliminado == 10:
                            sonido_milei.play()
                    elif enemigo["mask"] == BULRICH:
                        bulrich_eliminada += 1
                        if bulrich_eliminada == 10:
                            sonido_bulrich.play()
                    elif enemigo["mask"] == SCHIARETTI:
                        schiaretti_eliminado += 1
                        if schiaretti_eliminado == 10:
                            sonido_schiaretti.play()
                    elif enemigo["mask"] == BREGMAN:
                        bregman_eliminada += 1
                        if bregman_eliminada == 10:
                            sonido_bregman.play()

                    enemigos.remove(enemigo)
                    enemigos_eliminados += 1
                    score += 1
                # sacar el proyectil una vez que sale de la pantalla
                elif proyectil_jugador in proyectiles_jugador and proyectil_jugador["y"] + ALTO_VENTANA < ALTO_VENTANA - ALTO_PROYECTIL:
                    proyectiles_jugador.remove(proyectil_jugador)

        # Proyectiles enemigos

        for proyectil_enemigo in proyectiles_enemigos[:]:
            # proyectil_enemigos_disparados += 1
            offset = (jugador['x'] - proyectil_enemigo['x'],
                      jugador['y'] - proyectil_enemigo['y'])
            # Colision proyectil enemigo con jugador
            if proyectil_enemigo['mascara'].overlap(mascara_jugador, offset) != None:
                proyectiles_enemigos.remove(proyectil_enemigo)
                sonido_danio.play()
                vidas_jugador -= 1
            # sacar el proyectil una vez que sale de la pantalla
            elif proyectil_enemigo["y"] > ALTO_VENTANA:
                proyectiles_enemigos.remove(proyectil_enemigo)

            for vida in vidas_extras[:]:
                offset = (jugador['x'] - vida['x'],
                          jugador['y'] - vida['y'])
                if mascara_vida.overlap(mascara_jugador, offset) != None:
                    sonido_vida.play()
                    vidas_jugador += 1
                    vidas_extras.remove(vida)

            for power in power_up[:]:
                offset = (jugador['x'] - power['x'],
                          jugador['y'] - power['y'])
                if mascara_motosierra.overlap(mascara_jugador, offset) != None:
                    sonido_tiemblen.play()
                    proyectil_motosierra.append(motosierra_power)
                    if not motosierra_cargada:  # Bandera para que solo me sume 1 valor en poder cuando agarra el power up motosierra
                        poder = poder + 1
                        motosierra_cargada = True
                    power_up.remove(power)
                elif power["y"] > ALTO_VENTANA:
                    power_up.remove(power)

            for enemigo in enemigos[:]:
                for motosierra in proyectil_motosierra[:]:
                    offset = (enemigo['x'] - motosierra['x'],
                              enemigo['y'] - motosierra['y'])
                    if mascara_motosierra_power.overlap(enemigo['mascara'], offset) != None:
                        sonido_colision.play()
                        enemigos.remove(enemigo)
                        enemigos_eliminados += 1
                        score += 1
                    # sacar el proyectil una vez que sale de la pantalla
                    if motosierra in proyectil_motosierra and motosierra["x"] > ANCHO_VENTANA:
                        toasty = True
                        mover_sierra = False
                        proyectil_motosierra.remove(motosierra)
                        sonido_toasty.play()

        # Texto Score, vidas, pausaa

        texto_vidas = fuente_juego.render(
            f"Vidas: {vidas_jugador}", True, (BLANCO))
        texto_puntaje = fuente_juego.render(
            f"Puntaje: {score}", True, (BLANCO))
        texto_pausa = fuente_juego.render("P = Pausa", True, (BLANCO))
        texto_mute = fuente_juego.render("M = Mute", True, (BLANCO))
        texto_motosierra = fuente_juego.render(
            f"F = Motosierra ({poder})", True, (BLANCO))

        # Game Over 0 vidas
        if vidas_jugador <= 0:
            corriendo = False
            # print("¡Has perdido! Se acabaron las vidas.")
            pygame.mixer.music.pause()
            # Guardo el maximo score
            if score > highscore:
                highscore = score
                guardar_score(highscore)
                sonido_game_over_ganar.play()
                ventana_win(score)
            else:
                sonido_game_over_perder.play()
                ventana_game_over(score)
            menu_principal()
            bucle_juego()

        # Cada 50 enemigos eliminados vida extra
        if enemigos_eliminados == FILA_ENEMIGOS * COLUMNA_ENEMIGOS:
            if vida_extra["x"] == jugador["x"]:
                vida_extra = crear_vida_extra()
            vidas_extras.append(vida_extra)
            enemigos_eliminados = 0  # Reseteo para volver a contar enemigos
            # Reseteo para volver a reproducir sonidos
            massa_eliminado = 0
            milei_eliminado = 0
            bulrich_eliminada = 0
            schiaretti_eliminado = 0
            bregman_eliminada = 0
            enemigos = crear_grilla_enemigos()  # Vuelvo a crear enemigos
            # Reseteo el movimiento para que vuelvan a la posicion inicial
            direccion_movimiento_enemigo = 1
            vel_enemigos += 0.5  # Aumento la velocidad de los enemigos
            prob_disparo_enemigo += 2  # Aumento la probabilidad de disparo

        if score > 0 and score % 75 == 0:
            if not motosierra_on:  # Bandera para que solo me sume 1 power up
                power_up.append(motosierra)
                motosierra_on = True

        # Comienzo a dibujar la pantalla

        # rectangulo para cargar fondo
        fondo = pygame.Rect(0, 0, ANCHO_VENTANA, ALTO_VENTANA)
        ventana.blit(imagen_bkg, fondo)
        if vidas_extras:
            dibujar_power_up(vidas_extras)
        if power_up or poder > 0:
            dibujar_power_up(power_up)
            ventana.blit(texto_motosierra, (ANCHO_VENTANA // 2 -
                         TAMAÑO_BLOQUE, ALTO_VENTANA - 30))
        if proyectil_motosierra:
            dibujar_motosierra(motosierra_power)
        if toasty:
            dibujar_bloque(peron)
        dibujar_jugador(jugador)
        dibujar_enemigos(enemigos)
        # Dibujar proyectiles del jugador
        dibujar_proyectiles(proyectiles_jugador)
        # Dibujar proyectiles de los enemigos
        dibujar_proyectiles(proyectiles_enemigos)
        # Dibujar Score y vidas
        ventana.blit(texto_vidas, (10, 10))
        ventana.blit(texto_puntaje, (ANCHO_VENTANA - 140, 10))
        ventana.blit(texto_pausa, (10, ALTO_VENTANA - 30))
        ventana.blit(texto_mute, (ANCHO_VENTANA - 130, ALTO_VENTANA - 30))

        pygame.display.update()

    cerrar_juego()


bucle_juego()
# Bucle menu
menu_principal()
bucle_juego()
