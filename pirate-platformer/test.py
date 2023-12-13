import pygame
import sys

# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tamaño de la ventana
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Selector de Niveles")

# Fuente y tamaño del texto
font = pygame.font.Font(None, 36)

# Función para dibujar botones


def draw_buttons():
    level1_text = font.render("Nivel 1", True, WHITE)
    level2_text = font.render("Nivel 2", True, WHITE)
    level3_text = font.render("Nivel 3", True, WHITE)

    # Botones rectangulares
    level1_button = pygame.Rect(50, 50, 200, 50)
    level2_button = pygame.Rect(50, 120, 200, 50)
    level3_button = pygame.Rect(50, 190, 200, 50)

    # Dibujar botones
    pygame.draw.rect(screen, RED, level1_button)
    pygame.draw.rect(screen, GREEN, level2_button)
    pygame.draw.rect(screen, BLUE, level3_button)

    # Dibujar texto en botones
    screen.blit(level1_text, (65, 60))
    screen.blit(level2_text, (65, 130))
    screen.blit(level3_text, (65, 200))

    return level1_button, level2_button, level3_button


running = True
level_selected = None

while running:
    screen.fill((0, 0, 0))

    # Dibujar botones y obtener su posición
    level1_button, level2_button, level3_button = draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Verificar si se hizo clic en algún botón
            if level1_button.collidepoint(mouse_pos):
                level_selected = 1
            elif level2_button.collidepoint(mouse_pos):
                level_selected = 2
            elif level3_button.collidepoint(mouse_pos):
                level_selected = 3

    pygame.display.flip()
    print(level_selected)

# Luego, puedes usar la variable `level_selected` para llevar a cabo la acción correspondiente con el nivel seleccionado.
