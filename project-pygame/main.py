import pygame, sys

# lista -> [] -> mutable
# tupla -> () -> inmutable

l = [3, 4, 5]
t = (3, 4, 5)

pygame.init()

SIZE = (800, 600)

VENTANA = pygame.display.set_mode(SIZE)

VENTANA.fill((255,255,80))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()