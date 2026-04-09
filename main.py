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

#player properties
player_width = 40
player_height = 55
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 7

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed

    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Draw background
    screen.blit(background, (0, 0))

    # Draw player
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, (0, 200, 255), player_rect)

    # Update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()