import pygame
import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Coins")
clock = pygame.time.Clock()

# Background
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH+270, HEIGHT+50))

# Character
characters = {
    "jojo": {
        "image": pygame.image.load("assets/jojo.png"),
        "name": "Jojo"
    }
}
current_character = "jojo"

# Player
player_width = 50
player_height = 70
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 70
player_speed = 7

player_img = pygame.transform.scale(
    characters[current_character]["image"],
    (player_width, player_height)
)

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
big_font = pygame.font.SysFont(None, 60)

state = "menu"

running = True
while running:

    mouse_pos = pygame.mouse.get_pos()

    # SETTINGS
    settings_text = font.render("SETTINGS", True, (255,255,255))
    settings_rect = settings_text.get_rect(topleft=(20, 10))
    if settings_rect.collidepoint(mouse_pos):
        settings_text = font.render("SETTINGS", True, (255,220,100))

    # MENU TEXT
    start_text = font.render("START", True, (255,255,255))
    char_text = font.render("SELECT CHARACTER", True, (255,255,255))

    start_rect = start_text.get_rect(center=(WIDTH//2, 310))
    char_rect = char_text.get_rect(center=(WIDTH//2, 370))

    if start_rect.collidepoint(mouse_pos):
        start_text = font.render("START", True, (255,220,100))
    if char_rect.collidepoint(mouse_pos):
        char_text = font.render("SELECT CHARACTER", True, (255,220,100))

    # Character buttons
    ok_text = font.render("OK", True, (255,255,255))
    cancel_text = font.render("CANCEL", True, (255,255,255))

    ok_rect = ok_text.get_rect(center=(560, 280))
    cancel_rect = cancel_text.get_rect(center=(560, 340))

    if ok_rect.collidepoint(mouse_pos):
        ok_text = font.render("OK", True, (255,220,100))
    if cancel_rect.collidepoint(mouse_pos):
        cancel_text = font.render("CANCEL", True, (255,220,100))

    # Game over buttons
    retry_text = font.render("RETRY", True, (255,255,255))
    menu_text = font.render("MAIN MENU", True, (255,255,255))

    retry_rect = retry_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    menu_rect = menu_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))

    if retry_rect.collidepoint(mouse_pos):
        retry_text = font.render("RETRY", True, (255,220,100))
    if menu_rect.collidepoint(mouse_pos):
        menu_text = font.render("MAIN MENU", True, (255,220,100))

    title = big_font.render("Catch the Falling Coins", True, (255,255,255))
    title_rect = title.get_rect(center=(WIDTH//2, 150))

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    score = 0
                    lives = 3
                    game_over = False
                    coin_y = 0
                    player_x = WIDTH // 2 - player_width // 2
                    state = "game"

                if char_rect.collidepoint(event.pos):
                    state = "character_select"

        elif state == "character_select":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ok_rect.collidepoint(event.pos):
                    state = "menu"
                if cancel_rect.collidepoint(event.pos):
                    state = "menu"

        elif state == "game":
            if event.type == pygame.MOUSEBUTTONDOWN and game_over:
                if retry_rect.collidepoint(event.pos):
                    score = 0
                    lives = 3
                    coin_y = 50
                    game_over = False

                if menu_rect.collidepoint(event.pos):
                    state = "menu"
                    game_over = False

    # DRAW BACKGROUND (GLOBAL)
    screen.blit(background, (-50, 50))

    # RIBBON (ALL SCREENS)
    pygame.draw.rect(screen, (20, 20, 20), (0, 0, WIDTH, 50))
    pygame.draw.line(screen, (100, 100, 100), (0, 50), (WIDTH, 50), 2)

    # 🔥 SETTINGS ONLY IN MENU + CHARACTER SELECT
    if state in ["menu", "character_select"]:
        screen.blit(settings_text, settings_rect)

    # STATES
    if state == "menu":
        screen.blit(title, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(char_text, char_rect)

    elif state == "character_select":
        title2 = big_font.render("SELECT CHARACTER", True, (255,255,255))
        screen.blit(title2, title2.get_rect(center=(WIDTH//2, 80)))

        jojo_big = pygame.transform.scale(
            characters[current_character]["image"], (150, 210)
        )
        screen.blit(jojo_big, (150, 200))

        name_text = font.render(characters[current_character]["name"], True, (255,255,255))
        screen.blit(name_text, name_text.get_rect(center=(225, 430)))

        screen.blit(left_arrow, (90, 280))
        screen.blit(right_arrow, (330, 280))

        screen.blit(ok_text, ok_rect)
        screen.blit(cancel_text, cancel_rect)

    elif state == "game":
        if not game_over:
            keys = pygame.key.get_pressed()

            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0:
                player_x -= player_speed

            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < WIDTH - player_width:
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

        screen.blit(player_img, (player_x, player_y))
        screen.blit(coin_img, (coin_x, coin_y))

        for i in range(lives):
            screen.blit(heart_img, (20 + i * 40, 10))

        ui_coin_x = WIDTH - 120
        screen.blit(coin_img, (ui_coin_x, 2))

        score_text = font.render(f"{score}", True, (255,255,255))
        screen.blit(score_text, (ui_coin_x + coin_width + 5, 13))

        if game_over:
            over_text = big_font.render("GAME OVER", True, (255, 80, 80))
            screen.blit(over_text, over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 60)))

            screen.blit(retry_text, retry_rect)
            screen.blit(menu_text, menu_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()