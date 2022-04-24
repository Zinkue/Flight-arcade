import pygame
from pygame.locals import RLEACCEL
import random

class Planet(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Planet, self).__init__()
        self.width = width
        self.height = height
        self.sprites = ["images/Baren.png", "images/Ice.png",
                        "images/Lava.png", "images/Terran.png"]
        self.surface = pygame.image.load(
            self.sprites[random.randint(0, 3)]).convert()
        self.surface.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surface.get_rect(
            center=(
                random.randint(0, self.width),
                # Spawn the enemy off-screen
                random.randint(-125, -75))
        )
        self.speed = 2

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > self.height:
            self.kill()
