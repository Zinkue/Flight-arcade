import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from player import Player
from enemy import Enemy
from planet import Planet


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

# Initialize the player
player = Player(screen_width, screen_height)

# Create the groups for all sprites, other for the enemies and other for the planets
enemies = pygame.sprite.Group()
planets = pygame.sprite.Group()
all_sprites = pygame.sprite.LayeredUpdates()
all_sprites.add(player)

# Create the loop
running = True

while running:
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
        pygame.time.delay(500)

        # Reset the game
        player = Player(screen_width, screen_height)
        enemies = pygame.sprite.Group()
        planets = pygame.sprite.Group()
        all_sprites = pygame.sprite.LayeredUpdates()
        all_sprites.add(player)

    clock.tick(60)

    screen.fill((0, 0, 0))
