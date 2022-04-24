import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from player import Player


# Initialize the game
pygame.init()

# Define constants
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((0, 0, 0))

# Initialize the player and draw it on the screen
player = Player()
screen.blit(player.surface, player.rect)
pygame.display.flip()

# Create the loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
