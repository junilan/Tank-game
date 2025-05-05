import pygame
from .projectile import Projectile
import config
from src.utils import load_image
from src.entities.character_stats import TankStatus

class Shell(Projectile):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.speed = TankStatus["shell_speed"]

        image = load_image(config.IMAGEFILE_PATH + "bullet.png")

        #self.direction = -direction
        current_angle = self.direction.angle_to(pygame.Vector2(0, 1)) # Angle in degrees

        # 2. Rotate the original image
        rotated_shell_image = pygame.transform.rotate(image, current_angle)

        self.image = rotated_shell_image
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # Update the position of the shell based on its speed and direction
        
        movement = self.direction * self.speed 
        x ,y = self.rect.center
        x -= movement.x
        y -= movement.y
        self.rect.center = (int(x), int(y))

        if self.rect.left > config.WIDTH or self.rect.right < 0 or self.rect.top > config.HEIGHT or self.rect.bottom < 0:
            self.kill()
            
