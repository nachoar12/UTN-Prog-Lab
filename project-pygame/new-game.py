import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana del juego
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colores
ENEMY_COLORS = {
    "celeste": (0, 156, 222),
    "violeta": (117, 59, 189),
    "amarillo": (254, 221, 0),
    "azul": (67, 72, 143),
    "rojo": (249, 84, 97)
}

PLAYER_COLOR = (60, 179, 113)

# Tamaño de los bloques
BLOCK_SIZE = 50
ENEMY_ROWS = 5
ENEMY_COLS = 10
ENEMY_SPACING = 25
ENEMY_VELOCITY = 1  # Velocidad de los enemigos

# Crear jugador


def create_player():
    return {
        'x': WINDOW_WIDTH // 2 - BLOCK_SIZE // 2,
        'y': WINDOW_HEIGHT - BLOCK_SIZE * 2,
        'color': PLAYER_COLOR
    }

# Crear un enemigo con un color específico


def create_enemy(x, y, color):
    return {'x': x, 'y': y, 'color': color}

# Crear una función para dibujar un enemigo con un color específico


def draw_enemy_celeste(x, y):
    color = ENEMY_COLORS["celeste"]
    enemy = create_enemy(x, y, color)
    draw_block(enemy)


def draw_enemy_violeta(x, y):
    color = ENEMY_COLORS["violeta"]
    enemy = create_enemy(x, y, color)
    draw_block(enemy)


def draw_enemy_amarillo(x, y):
    color = ENEMY_COLORS["amarillo"]
    enemy = create_enemy(x, y, color)
    draw_block(enemy)


def draw_enemy_azul(x, y):
    color = ENEMY_COLORS["azul"]
    enemy = create_enemy(x, y, color)
    draw_block(enemy)


def draw_enemy_rojo(x, y):
    color = ENEMY_COLORS["rojo"]
    enemy = create_enemy(x, y, color)
    draw_block(enemy)

# Dibujar bloque


def draw_block(block):
    pygame.draw.rect(win, block['color'], (block['x'],
                     block['y'], BLOCK_SIZE, BLOCK_SIZE))

# Dibujar una fila de enemigos


# def draw_enemy_row(y):
#     enemies = []
#     for col in range(ENEMY_COLS):
#         x = col * (BLOCK_SIZE + ENEMY_SPACING)
#         color = color = random.choice(list(ENEMY_COLORS.values()))
#         enemy = create_enemy(x, y, color)
#         enemies.append(enemy)
#         draw_block(enemy)
#     return enemies

def draw_enemy_row(y):
    enemies = []
    draw_enemy_celeste(0, y)
    draw_enemy_violeta(BLOCK_SIZE + ENEMY_SPACING, y)
    draw_enemy_amarillo((BLOCK_SIZE + ENEMY_SPACING) * 2, y)
    draw_enemy_azul((BLOCK_SIZE + ENEMY_SPACING) * 3, y)
    draw_enemy_rojo((BLOCK_SIZE + ENEMY_SPACING) * 4, y)
    enemies.extend([
        create_enemy(0, y, ENEMY_COLORS["celeste"]),
        create_enemy(BLOCK_SIZE + ENEMY_SPACING, y, ENEMY_COLORS["violeta"]),
        create_enemy((BLOCK_SIZE + ENEMY_SPACING) *
                     2, y, ENEMY_COLORS["amarillo"]),
        create_enemy((BLOCK_SIZE + ENEMY_SPACING)
                     * 3, y, ENEMY_COLORS["azul"]),
        create_enemy((BLOCK_SIZE + ENEMY_SPACING) * 4, y, ENEMY_COLORS["rojo"])
    ])
    return enemies


# Mover jugador


def move_player(keys, player, vel):
    if keys[pygame.K_LEFT] and player['x'] > vel:
        player['x'] -= vel
    if keys[pygame.K_RIGHT] and player['x'] < WINDOW_WIDTH - BLOCK_SIZE - vel:
        player['x'] += vel

# Mover los enemigos horizontalmente


def move_enemies(enemies, enemy_velocity):
    for enemy in enemies:
        enemy['x'] += enemy_velocity

# Revisar bordes de los enemigos y cambiar dirección


def check_enemy_edges(enemies):
    for enemy in enemies:
        if enemy['x'] <= 0 or enemy['x'] >= WINDOW_WIDTH - BLOCK_SIZE:
            return True
    return False


# Loop del juego
def game_loop():
    player = create_player()
    enemies = []
    for row in range(ENEMY_ROWS):
        enemy_row = draw_enemy_row(row * (BLOCK_SIZE + ENEMY_SPACING))
        enemies.extend(enemy_row)

    vel = 5
    enemy_velocity = 1  # Velocidad de los enemigos
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60 * 50)
        win.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        move_player(keys, player, vel)

        for enemy in enemies:
            enemy['x'] += enemy_velocity

        for enemy in enemies:
            if enemy['x'] <= 0 or enemy['x'] >= WINDOW_WIDTH - BLOCK_SIZE:
                enemy_velocity *= -1
                for e in enemies:
                    e['y'] += 10
                break

        draw_block(player)
        for enemy in enemies:
            draw_block(enemy)

        pygame.display.update()

    pygame.quit()


# Iniciar el juego
game_loop()
