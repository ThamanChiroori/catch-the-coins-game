import pygame
import sys
import random

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Coins")

# Load background
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Player
player_width = 40
player_height = 55
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 7

# Coin
coin_width = 15
coin_height = 15
coin_x = random.randint(0, WIDTH - coin_width)
coin_y = 0
coin_speed = 5

# Game data
score = 0
lives = 3
game_over = False

font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Restart
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                player_x = WIDTH // 2 - player_width // 2
                coin_x = random.randint(0, WIDTH - coin_width)
                coin_y = 0
                score = 0
                lives = 3
                game_over = False

    # Draw background
    screen.blit(background, (0, 50))

    # Draw ribbon
    ribbon_height = 50
    pygame.draw.rect(screen, (20, 20, 20), (0, 0, WIDTH, ribbon_height))
    pygame.draw.line(screen, (100, 100, 100), (0, ribbon_height), (WIDTH, ribbon_height), 2)

    if not game_over:
        # Movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed

        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # Coin movement
        coin_y += coin_speed

        # Missed coin
        if coin_y > HEIGHT:
            coin_y = 0
            coin_x = random.randint(0, WIDTH - coin_width)
            lives -= 1

        # Rects
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        coin_rect = pygame.Rect(coin_x, coin_y, coin_width, coin_height)

        # Collision
        if player_rect.colliderect(coin_rect):
            score += 1
            coin_y = 0
            coin_x = random.randint(0, WIDTH - coin_width)

        # Game over check
        if lives <= 0:
            game_over = True

    else:
        # Still need rects for drawing
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        coin_rect = pygame.Rect(coin_x, coin_y, coin_width, coin_height)

    # Draw player & coin
    pygame.draw.rect(screen, (0, 200, 255), player_rect)
    pygame.draw.rect(screen, (255, 215, 0), coin_rect)

    # UI text
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))

    screen.blit(score_text, (20, 10))
    screen.blit(lives_text, (WIDTH - 150, 10))

    # Game Over text
    if game_over:
        over_text = font.render("GAME OVER - Press R to Restart", True, (255, 80, 80))
        text_rect = over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(over_text, text_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()