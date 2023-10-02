from config import *

def generate_random_color():
    from random import randint
    """
    Generates a random color using RGB values.

    Returns:
    tuple: An RGB tuple representing the randomly generated color.
    """
    # Generate random RGB values in the range 0-255 for each color component
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)

    return random_red, random_green, random_blue

# direcciones
UPRIGHT = 9
DOWNRIGHT = 3
DOWNLEFT = 1
UPLEFT = 7


def get_random_direction():
    """
    Returns a random direction from the set of upright, downright, upleft, downleft.

    Returns:
    constant: A randomly chosen direction (upright, downright, upleft, or downleft).
    """
    from random import choice
    direcciones = [UPRIGHT, DOWNRIGHT, DOWNLEFT, DOWNRIGHT]
    return choice(direcciones)

# dimensiones del rectangulo
BLOCK_WIDTH = 25
BLOCK_HEIGHT = 25

def create_blocks(num):
    """
    Create a specified number of blocks and return a list of dictionaries.

    Parameters:
    num_blocks (int): The number of blocks to create.

    Returns:
    list: A list of dictionaries representing the blocks.
    """
    bloques = []

    for i in range(num):
        import pygame

        rect = pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT)
        color = generate_random_color()
        dir = get_random_direction()

        block_dict = {"rect": rect, "color": color, "dir": dir}
        bloques.append(block_dict)

    return bloques
