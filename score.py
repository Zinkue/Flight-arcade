import pygame


# Create the score display
class Score(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Score, self).__init__()
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("arialblack.ttf", 80)
        self.score = 0
        self.surface = self.font.render("0", True, (255, 255, 255))
        self.rect = self.surface.get_rect(midtop=(self.width/2, 0))
        self._layer = 4

    def update(self):
        self.score += 1
        self.surface = self.font.render(str(self.score), True, (255, 255, 255))
