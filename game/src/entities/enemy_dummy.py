import pygame
from .unit import Unit

class EnemyDummy(Unit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((50, 50)) 
        self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect()

    def update(self, dt):
        pass
       
