import pygame
from pygame.locals import RLEACCEL
import random


# Define the enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Enemy, self).__init__()
        self.width = width
        self.height = height
        self.sprites = ["images/meteor.png", "images/flaming_meteor.png"]
        self.surface = pygame.image.load(
            self.sprites[random.randint(0, 1)]).convert()
        self.surface.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surface.get_rect(
            center=(
                random.randint(0, self.width),
                # Spawn the enemy off-screen
                random.randint(-100, -50))
        )
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > self.height:
            self.kill()
