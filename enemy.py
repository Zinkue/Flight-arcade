import pygame
import random


# Define the enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Enemy, self).__init__()
        self.width = width
        self.height = height
        self.surface = pygame.Surface((10, 25))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect(
            center=(
                random.randint(0, self.width),
                # Spawn the enemy off-screen
                random.randint(-100, -50))
        )
        self.speed = random.randint(5, 15)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > self.height:
            self.kill()
