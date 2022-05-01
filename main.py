import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
    K_r
)
from player import Player
from enemy import Enemy
from planet import Planet
from score import Score
from menu import StartMenu, RestartMenu


# Initialize the game
pygame.init()

# Define constants
screen_width = 500
screen_height = 650

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("images/background_stars.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Setup the clock for framerate
clock = pygame.time.Clock()

# Create a custom event to add a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Create a custom event to add a new planet
ADDPLANET = pygame.USEREVENT + 2
pygame.time.set_timer(ADDPLANET, 5000)

# Create a custom event to increment the score
ADDSCORE = pygame.USEREVENT + 3
pygame.time.set_timer(ADDSCORE, 1000)

# Initialize the player
player = Player(screen_width, screen_height)

# Initialize the score
score = Score(screen_width, screen_height)

# Initialize the start menu
start_menu = StartMenu(screen_width, screen_height)

# Create the groups for all sprites, enemies, planets
enemies = pygame.sprite.Group()
planets = pygame.sprite.Group()
all_sprites = pygame.sprite.LayeredUpdates()
all_sprites.add(player)
all_sprites.add(score)

# Create the loop
running = True
start_menu_running = True

# Initialize the start menu
while start_menu_running:
    clock.tick(10)
    screen.blit(background, (0, 0))
    screen.blit(start_menu.surface_1, start_menu.rect_1)
    screen.blit(start_menu.surface_2, start_menu.rect_2)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                start_menu_running = False
                running = False

            elif event.key == K_SPACE:
                start_menu_running = False

        elif event.type == QUIT:
            start_menu_running = False
            running = False

    pygame.display.flip()

# Initialize the game
while running:
    clock.tick(60)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy(screen_width, screen_height)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDPLANET:
            new_planet = Planet(screen_width, screen_height)
            planets.add(new_planet)
            all_sprites.add(new_planet)
        elif event.type == ADDSCORE:
            score.update()

    # Get user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()

    # Update planet position
    planets.update()

    for entity in all_sprites:
        screen.blit(entity.surface, entity.rect)

    pygame.display.flip()

    # Check for collisions between enemy and player
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

        # Initialize the restart menu
        restart_menu = RestartMenu(screen_width, screen_height, score.score)
        restart_menu_running = True
        while restart_menu_running:
            clock.tick(10)
            screen.blit(background, (0, 0))
            screen.blit(restart_menu.surface_1, restart_menu.rect_1)
            screen.blit(restart_menu.surface_2, restart_menu.rect_2)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        restart_menu_running = False
                        running = False

                    elif event.key == K_r:
                        restart_menu_running = False

                elif event.type == QUIT:
                    restart_menu_running = False
                    running = False

            pygame.display.flip()

        # Reset the game elements
        player = Player(screen_width, screen_height)
        score = Score(screen_width, screen_height)
        enemies = pygame.sprite.Group()
        planets = pygame.sprite.Group()
        all_sprites = pygame.sprite.LayeredUpdates()
        all_sprites.add(player)
        all_sprites.add(score)
