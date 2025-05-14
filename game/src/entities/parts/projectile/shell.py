import pygame
from .projectile import Projectile
import config
from src.utils import load_image
from src.entities.character_stats import TANKSTATUS

class Shell(Projectile):
    '''
    Shell class that represents a projectile fired from the tank's cannon.
    
    Attributes:
        x (int): The x-coordinate of the shell.
        y (int): The y-coordinate of the shell.
        direction (pygame.math.Vector2): The direction of the shell.
        speed (float): The speed of the shell.
        image (pygame.Surface): The image representing the shell.
        mask (pygame.mask.Mask): The mask for collision detection.
        rect (pygame.Rect): The rectangle representing the shell's position and size.
    '''
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        projectile_name  = "shell"
        self.speed = TANKSTATUS[projectile_name + "_speed"]
        
        self.image = self.set_image(projectile_name)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (x, y))
        self.rect.inflate(-100, -50)