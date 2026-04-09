import pygame
import sys

# Initialize pygame
pygame.init()

# Recommended resolution
WIDTH = 800
HEIGHT = 600

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Coins")

# Load background image
background = pygame.image.load("assets/background.png")

# Scale background to fit screen
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background, (0, 0))

    # Update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()