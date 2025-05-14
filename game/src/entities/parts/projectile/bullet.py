import pygame
from .projectile import Projectile
import config
from src.utils import load_image
from src.entities.character_stats import TANKSTATUS

class Bullet(Projectile):
    '''
    Bullet class that represents a projectile fired from the tank's machine gun.

    Attributes:
        x (int): The x-coordinate of the bullet.
        y (int): The y-coordinate of the bullet.
        direction (pygame.math.Vector2): The direction of the bullet.
        speed (float): The speed of the bullet.
        image (pygame.Surface): The image representing the bullet.
        mask (pygame.mask.Mask): The mask for collision detection.
        rect (pygame.Rect): The rectangle representing the bullet's position and size.
    '''
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.direction = direction
        projectile_name  = "bullet"
        self.speed = TANKSTATUS[projectile_name + "_speed"]

        self.loaded_image = load_image(config.IMAGEFILE_PATH + projectile_name + ".png")
        
        self.image = self.set_image(projectile_name)
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect(center = (x, y))