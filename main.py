import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from player import Player
from enemy import Enemy


# Initialize the game
pygame.init()

# Define constants
screen_width = 500
screen_height = 650

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Setup the clock for framerate
clock = pygame.time.Clock()

# Create a custom event to add a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Initialize the player
player = Player(screen_width, screen_height)

# Create the groups for all sprites and other for the enemies
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create the loop
running = True

while running:
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

    # Get user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()

    for entity in all_sprites:
        screen.blit(entity.surface, entity.rect)

    pygame.display.flip()

    clock.tick(60)

    screen.fill((0, 0, 0))
