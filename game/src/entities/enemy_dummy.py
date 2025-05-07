import pygame
from .unit import Unit

class EnemyDummy(Unit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.rect = pygame.Rect(x, y, 50, 50)

    def update(self, dt):
        pass
       

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)