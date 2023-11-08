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

        dibujar_jugador(jugador)
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
