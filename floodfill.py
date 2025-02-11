import pygame
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flood Fill Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FILL_COLOR = (255, 0, 0)  # Red

# Draw a simple boundary (rectangle)
pygame.draw.rect(screen, BLACK, (100, 100, 300, 300), 3)
pygame.display.update()

def flood_fill_iterative(x, y, target_color, replacement_color):
    """Iterative flood fill using a stack to prevent recursion depth errors."""
    if target_color == replacement_color:
        return

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        # Bounds check
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            continue

        # Get the current color at (x, y)
        current_color = screen.get_at((x, y))[:3]  # Ignore alpha value

        # Fill only if it's the target color
        if current_color == target_color:
            pygame.draw.rect(screen, replacement_color, (x, y, 1, 1))
            pygame.display.update()
            pygame.time.delay(1)  # Delay to show filling step-by-step

            # Push adjacent pixels onto the stack
            stack.append((x + 1, y))  # Right
            stack.append((x - 1, y))  # Left
            stack.append((x, y + 1))  # Down
            stack.append((x, y - 1))  # Up

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            target_color = screen.get_at((x, y))[:3]  # Original color at click
            flood_fill_iterative(x, y, target_color, FILL_COLOR)

pygame.quit()
