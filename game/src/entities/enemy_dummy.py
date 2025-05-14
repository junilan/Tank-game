import pygame
from .unit import Unit

class EnemyDummy(Unit):
    '''
    Enemy Dummy class that inherits from Unit.

    Attributes:
        image (pygame.Surface): The image of the enemy dummy.
        rect (pygame.Rect): The rectangle representing the position and size of the enemy dummy.
        mask (pygame.mask.Mask): The mask for collision detection.
    '''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((50, 50)) 
        self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        pass
       
