import pygame

# Initialize Pygame
pygame.init()

# Constants for window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Scale factor for the figure
SCALE_FACTOR = 0.5

# Initialize the screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flying Person")

# Function to draw the flying person
def draw_flying_person(x, y):
    # Scale down the dimensions
    scaled_width = int(50 * SCALE_FACTOR)
    scaled_height = int(100 * SCALE_FACTOR)

    # Draw the torso (rectangle for the suit)
    pygame.draw.rect(screen, BLUE, (x, y + 2 * scaled_height, scaled_width, scaled_height))

    # Draw the head (circle for messy hair)
    pygame.draw.circle(screen, BLACK, (x + int(scaled_width / 2), y + int(1.5 * scaled_height)), int(20 * SCALE_FACTOR))

    # Draw the arms (rectangles)
    arm_width = int(25 * SCALE_FACTOR)
    pygame.draw.rect(screen, BLUE, (x - arm_width, y + 2 * scaled_height, arm_width, int(10 * SCALE_FACTOR)))
    pygame.draw.rect(screen, BLUE, (x + scaled_width, y + 2 * scaled_height, arm_width, int(10 * SCALE_FACTOR)))

    # Draw the legs (rectangles)
    leg_width = int(15 * SCALE_FACTOR)
    pygame.draw.rect(screen, BLUE, (x, y + 3 * scaled_height, leg_width, int(50 * SCALE_FACTOR)))
    pygame.draw.rect(screen, BLUE, (x + int(35 * SCALE_FACTOR), y + 3 * scaled_height, leg_width, int(50 * SCALE_FACTOR)))

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update and draw the flying person
    draw_flying_person(375, 100)

    # Update the screen
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
