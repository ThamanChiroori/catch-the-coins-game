import pygame
import sys
import random

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

# coin properties
coin_width = 20
coin_height = 20
coin_x = random.randint(0, WIDTH - coin_width)
coin_y = 0
coin_speed = 5

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

    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = 0
        coin_x = random.randint(0, WIDTH - coin_width)

    # Draw background
    screen.blit(background, (0, 0))

    # Draw coin
    coin_rect = pygame.Rect(coin_x, coin_y, coin_width, coin_height)
    pygame.draw.rect(screen, (255, 215, 0), coin_rect)

    # Draw player
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, (0, 200, 255), player_rect)

    # Update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()