import pygame


# Create the start menu display
class StartMenu(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(StartMenu, self).__init__()
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("arialblack.ttf", 45)
        self.text_1 = "Welcome to Flight Arcade"
        self.surface_1 = self.font.render(self.text_1, True, (255, 255, 255))
        self.rect_1 = self.surface_1.get_rect(midtop=(self.width / 2, self.height / 2 - 100))
        self.text_2 = "Press SPACE to start the game"
        self.surface_2 = self.font.render(self.text_2, True, (255, 255, 255))
        self.rect_2 = self.surface_2.get_rect(midtop=(self.width/2, self.height / 2 - 50))
        self._layer = 2


class RestartMenu(pygame.sprite.Sprite):
    def __init__(self, width, height, score):
        super(RestartMenu, self).__init__()
        self.width = width
        self.height = height
        self.score = score
        self.font = pygame.font.SysFont("arialblack.ttf", 45)
        self.text_1 = f"Your score was: {self.score}"
        self.surface_1 = self.font.render(self.text_1, True, (255, 255, 255))
        self.rect_1 = self.surface_1.get_rect(midtop=(self.width / 2, self.height / 2 - 100))
        self.text_2 = "Press R to start the game"
        self.surface_2 = self.font.render(self.text_2, True, (255, 255, 255))
        self.rect_2 = self.surface_2.get_rect(midtop=(self.width/2, self.height / 2 - 50))
        self._layer = 2
