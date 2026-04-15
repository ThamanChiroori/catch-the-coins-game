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

# Load background (your values kept)
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH+270, HEIGHT+50))

# Player
player_width = 50
player_height = 70
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 70
player_speed = 7

# Player image
player_img = pygame.image.load("assets/jojo.png")
player_img = pygame.transform.scale(player_img, (player_width, player_height))

# Coin
coin_width = 45
coin_height = 45
coin_x = random.randint(0, WIDTH - coin_width)
coin_y = 0
coin_speed = 5

coin_img = pygame.image.load("assets/coin.png")
coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))

# Heart
heart_img = pygame.image.load("assets/heart.png")
heart_img = pygame.transform.scale(heart_img, (30, 30))

# Arrows
left_arrow = pygame.image.load("assets/leftArrow.png")
right_arrow = pygame.image.load("assets/rightArrow.png")
left_arrow = pygame.transform.scale(left_arrow, (40, 40))
right_arrow = pygame.transform.scale(right_arrow, (40, 40))

# Game data
score = 0
lives = 3
game_over = False

font = pygame.font.SysFont(None, 36)

# State system
state = "menu"
selected_character = "jojo"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ========= MENU =========
        if state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if 350 < mx < 450 and 300 < my < 330:
                    state = "game"

                if 300 < mx < 500 and 350 < my < 380:
                    state = "character_select"

        # ===== CHARACTER SELECT =====
        elif state == "character_select":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if 500 < mx < 600 and 250 < my < 280:  # OK
                    selected_character = "jojo"
                    state = "menu"

                if 500 < mx < 650 and 300 < my < 330:  # CANCEL
                    state = "menu"

        # ========= GAME =========
        elif state == "game":
            if event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r:
                    state = "menu"
                    game_over = False

            if event.type == pygame.MOUSEBUTTONDOWN and game_over:
                mx, my = pygame.mouse.get_pos()

                # Retry
                if 350 < mx < 450 and 300 < my < 330:
                    player_x = WIDTH // 2 - player_width // 2
                    coin_x = random.randint(0, WIDTH - coin_width)
                    coin_y = 50
                    score = 0
                    lives = 3
                    game_over = False

                # Main menu
                if 320 < mx < 480 and 340 < my < 370:
                    state = "menu"
                    game_over = False

    # ========= DRAW =========

    # ----- MENU -----
    if state == "menu":
        screen.blit(background, (0, 0))

        title = font.render("Catch the Falling Coins", True, (255,255,255))
        start_text = font.render("START", True, (255,255,255))
        char_text = font.render("SELECT CHARACTER", True, (255,255,255))

        screen.blit(title, (WIDTH//2 - 150, 150))
        screen.blit(start_text, (WIDTH//2 - 50, 300))
        screen.blit(char_text, (WIDTH//2 - 120, 350))

    # ----- CHARACTER SELECT -----
    elif state == "character_select":
        screen.blit(background, (0, 0))

        title = font.render("SELECT CHARACTER", True, (255,255,255))
        screen.blit(title, (WIDTH//2 - 150, 50))

        jojo_big = pygame.transform.scale(player_img, (150, 210))
        screen.blit(jojo_big, (150, 200))

        screen.blit(left_arrow, (100, 260))
        screen.blit(right_arrow, (330, 260))

        ok_text = font.render("OK", True, (255,255,255))
        cancel_text = font.render("CANCEL", True, (255,255,255))

        screen.blit(ok_text, (500, 250))
        screen.blit(cancel_text, (500, 300))

    # ----- GAME -----
    elif state == "game":
        screen.blit(background, (-50, 50))

        # Ribbon
        pygame.draw.rect(screen, (20, 20, 20), (0, 0, WIDTH, 50))
        pygame.draw.line(screen, (100, 100, 100), (0, 50), (WIDTH, 50), 2)

        if not game_over:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed

            if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
                player_x += player_speed

            coin_y += coin_speed

            if coin_y > HEIGHT:
                coin_y = 50
                coin_x = random.randint(0, WIDTH - coin_width)
                lives -= 1

            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
            coin_rect = pygame.Rect(coin_x, coin_y, coin_width, coin_height)

            if player_rect.colliderect(coin_rect):
                score += 1
                coin_y = 0
                coin_x = random.randint(0, WIDTH - coin_width)

                coin_speed = min(10, 5 + score // 6)
                player_speed = min(12, 7 + score // 7)

            if lives <= 0:
                game_over = True
        else:
            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

        # Draw player
        screen.blit(player_img, (player_x, player_y))

        # Draw coin
        screen.blit(coin_img, (coin_x, coin_y))

        # Hearts
        for i in range(lives):
            screen.blit(heart_img, (20 + i * 40, 10))

        # Coin UI
        ui_coin_x = WIDTH - 120
        ui_coin_y = 2
        screen.blit(coin_img, (ui_coin_x, ui_coin_y))

        score_text = font.render(f"{score}", True, (255, 255, 255))
        screen.blit(score_text, (ui_coin_x + coin_width + 5, 13))

        # Game over UI
        if game_over:
            over_text = font.render("GAME OVER", True, (255, 80, 80))
            retry_text = font.render("RETRY", True, (255,255,255))
            menu_text = font.render("MAIN MENU", True, (255,255,255))

            screen.blit(over_text, (WIDTH//2 - 100, HEIGHT//2 - 50))
            screen.blit(retry_text, (WIDTH//2 - 50, HEIGHT//2))
            screen.blit(menu_text, (WIDTH//2 - 80, HEIGHT//2 + 40))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()