import pygame
from config import *

# Inicialización de Pygame
pygame.init()


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
