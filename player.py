import pygame


# Define the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((50, 20))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()
