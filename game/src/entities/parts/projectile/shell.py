import pygame
from .projectile import Projectile
import config
from src.utils import load_image
from src.entities.character_stats import TANKSTATUS

class Shell(Projectile):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        projectile_name  = "shell"
        self.speed = TANKSTATUS[projectile_name + "_speed"]

        #self.loaded_image = load_image(config.IMAGEFILE_PATH + projectile_name + ".png")
        
        self.image = self.set_image(projectile_name)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (x, y))
        self.rect.inflate(-100, -50)
        #self.mask = pygame.mask.from_surface(self.image)