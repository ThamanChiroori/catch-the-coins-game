import pygame
import sys
import random

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Coins")
clock = pygame.time.Clock()

# Load background
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Player
player_width = 50
player_height = 70
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 70
player_speed = 7

# 👉 Load player image (NEW)
player_img = pygame.image.load("assets/jojo.png")
player_img = pygame.transform.scale(player_img, (player_width, player_height))

# Coin
coin_width = 45
coin_height = 45
coin_x = random.randint(0, WIDTH - coin_width)
coin_y = 0
coin_speed = 5

# Load coin image
coin_img = pygame.image.load("assets/coin.png")
coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))

# Load heart image
heart_img = pygame.image.load("assets/heart.png")
heart_img = pygame.transform.scale(heart_img, (30, 30))

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

        # Restart game
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

    # Top ribbon
    ribbon_height = 50
    pygame.draw.rect(screen, (20, 20, 20), (0, 0, WIDTH, ribbon_height))
    pygame.draw.line(screen, (100, 100, 100), (0, ribbon_height), (WIDTH, ribbon_height), 2)

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed

        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        coin_y += coin_speed

        if coin_y > HEIGHT:
            coin_y = 0
            coin_x = random.randint(0, WIDTH - coin_width)
            lives -= 1

        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        coin_rect = pygame.Rect(coin_x, coin_y, coin_width, coin_height)

        if player_rect.colliderect(coin_rect):
            score += 1
            coin_y = 0
            coin_x = random.randint(0, WIDTH - coin_width)

        if lives <= 0:
            game_over = True
    else:
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # 👉 Draw player IMAGE instead of rectangle
    screen.blit(player_img, (player_x, player_y))

    # Draw coin
    screen.blit(coin_img, (coin_x, coin_y))

    # Draw hearts for lives
    for i in range(lives):
        screen.blit(heart_img, (20 + i * 40, 10))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH - 150, 10))

    # Game over text
    if game_over:
        over_text = font.render("GAME OVER - Press R to Restart", True, (255, 80, 80))
        text_rect = over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(over_text, text_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()