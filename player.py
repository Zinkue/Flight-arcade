import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)


# Define the player
class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Player, self).__init__()
        self.width = width
        self.height = height
        self.surface = pygame.Surface((20, 50))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect(center=(self.width/2, self.height))

    # Move the player
    def update_position(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep the player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.width:
            self.rect.right = self.width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.height:
            self.rect.bottom = self.height
