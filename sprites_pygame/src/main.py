import pygame


pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)


def get_image(hoja_sprites, frame, width, height, escala=1, color=(0, 0, 0)):
    imagen = pygame.Surface((width, height))
    hoja_sprites.set_clip((frame * width, frame * height, width, height))
    frame = hoja_sprites.subsurface(hoja_sprites.get_clip())
    imagen.set_colorkey(color)
    imagen.blit(frame, (0, 0))
    imagen = pygame.transform.scale(imagen, (width * escala, height * escala))
    return imagen


clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprites en pygame")

hoja_sprites = pygame.image.load(
    "sprites_pygame/assets/img/Crab_Sprite_Sheet.png")

ultima_actualizacion = pygame.time.get_ticks()
frame = 0
cant_frames = 4

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player = get_image(hoja_sprites, frame, 24, 24, 2)

    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultima_actualizacion >= 200:
        frame += 1
        if frame >= cant_frames:
            frame = 0

        ultima_actualizacion = tiempo_actual

    screen.fill((200, 200, 200))

    screen.blit(player, (0, 0))

    screen.blit(hoja_sprites, (0, 0))

    pygame.display.update()

pygame.quit()
