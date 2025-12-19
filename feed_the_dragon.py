import pygame, random

# Initialize pygame
pygame.init()

def make_text(font_object, text, color, background_color):
    return font_object.render(text, True, color, background_color)

def blit(surface, item, rect):
    surface.blit(item, rect)

def fill(surface, color):
    surface.fill(color)


def update_display():
    def draw(surface):
        pass
    pygame.display.update()


# Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")


# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


# Set game values
PLAYER_STARTING_LIVES = 0
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

# Set colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Set fonts
font = pygame.font.Font("assets/AttackGraffiti.ttf", 32)



score_text = make_text(font, f"Score: {score}", GREEN, DARK_GREEN)
title_text = make_text(font, f"Feed the Dragon", GREEN, WHITE)
lives_text = make_text(font, f"Lives: {score}", GREEN, DARK_GREEN)

score_rect = score_text.get_rect()
title_rect = title_text.get_rect()
lives_rect = title_text.get_rect()

score_rect.topleft = (10, 10)
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 10
lives_rect.topright = (-10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)

# Set sounds and music
coin_sound = pygame.mixer.Sound("assets/coin_sound.wav")
miss_sound = pygame.mixer.Sound("assets/miss_sound.wav")
miss_sound.set_volume(0.1)
pygame.mixer.music.load("assets/ftd_background_music.wav")




# Set images
player_image = pygame.image.load("assets/dragon_right.png")
player_rect = player_image.get_rect()
player_rect.x = 32
player_rect.y = WINDOW_HEIGHT // 2

coin_image = pygame.image.load("assets/coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)



# The main game loop
running = True
pygame.mixer.music.play(-1)

def tick():
    clock.tick(FPS)


def is_still_running():
    global running
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False


def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY



def handle_coin():
    global player_lives
    coin_rect.x -= coin_velocity
    if coin_rect.x < 0:
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)



def handle_collisions():
    # TODO:
    #   - Check if the player_rect and coin_rect are colliding using colliderect(...)
    #   - If they collide:
    #       * Increase score by 1
    #       * Play the coin sound
    #       * Increase coin_velocity by COIN_ACCELERATION
    #       * Reset the coin's position:
    #           - x: WINDOW_WIDTH + BUFFER_DISTANCE
    #           - y: random integer between the same top and bottom margins
    player_rect.y += coin_rect.y
    if player_rect.y < 0:
        colliderect(player_rect, coin_rect)
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)


def update_hud():
    # TODO:
    #   - Re-create score_text and lives_text each frame using make_text(...),
    #     so they show the updated score and lives values.
    #   - Remember to use the same font and colors (GREEN and DARKGREEN).
    score_text = title_text.get_rect(GREEN, True , DARK_GREEN)
    lives_text = title_text.get_rect(GREEN, True , DARK_GREEN)



def game_over_check():
    # TODO:
    #   - If player_lives reaches 0:
    #       * Draw the game over text and the "press any key to play again" text on the screen.
    #       * Update the display so the player can see the game over screen.
    #       * Stop the background music.
    #       * Create a loop (e.g., is_paused = True) that:
    #           - Waits for events:
    #               + If the player presses any key (KEYDOWN):
    #                   · Reset score to 0
    #                   · Reset player_lives to PLAYER_STARTING_LIVES
    #                   · Reset player position to center vertically
    #                   · Reset coin_velocity to COIN_STARTING_VELOCITY
    #                   · Restart the background music
    #                   · Exit the pause loop (resume game)
    #               + If the player clicks the window close button (QUIT):
    #                   · Set running to False and exit the pause loop so the game can end.
    if player_lives == 0:
        title_text.set_text("GAME OVER", True, DARK_GREEN)
        title_text.set_text("Press any key to play again", True, DARK_GREEN)
        update_display()




def update_screen():
    # TODO:
    #   - Fill the display_surface with a background color (e.g., BLACK) using your fill(...) helper.
    #   - Draw the HUD elements on the screen:
    #       * score_text, title_text, lives_text at their rect positions using your blit(...) helper.
    #   - Draw a horizontal line across the screen near the top to separate the HUD from the play area.
    #   - Draw the player image and the coin image at their rect positions using your blit(...) helper.
    #   - Finally, call update_display() so that everything appears on the screen.



while running:
    # Main game loop steps:
    #   1. Handle quit events.
    #   2. Move the player based on keyboard input.
    #   3. Move the coin and handle misses.
    #   4. Check for collisions between player and coin.
    #   5. Update the HUD text to match the current score and lives.
    #   6. Check if the game is over and either reset or quit.
    #   7. Draw everything on the screen.
    #   8. Tick the clock to control the frame rate.

    is_still_running()
    move_player()
    handle_coin()
    handle_collisions()
    update_hud()
    game_over_check()
    update_screen()
    tick()

# End the game
pygame.quit()
