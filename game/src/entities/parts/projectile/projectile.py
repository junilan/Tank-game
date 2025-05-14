import pygame  
from src.utils import load_image, calculate_angle_vec_to_degrees_rotate, movement_vector
import config

class Projectile(pygame.sprite.Sprite):
    '''
    Projectile class that represents a generic projectile fired from a tank.

    Attributes:
        x (int): The x-coordinate of the projectile.
        y (int): The y-coordinate of the projectile.
        direction (pygame.math.Vector2): The direction of the projectile.
        speed (float): The speed of the projectile.
        image (pygame.Surface): The image representing the projectile.
        mask (pygame.mask.Mask): The mask for collision detection.
        rect (pygame.Rect): The rectangle representing the projectile's position and size.
    '''
    def __init__(self, x, y, direction):
        super().__init__()
        self.direction = -direction
        self.speed = 0
        self.x, self.y = x, y


    def update(self, dt):
        # Update the position of the shell based on its speed and direction
        self.rect.center = movement_vector(self.rect.centerx, self.rect.centery, self.direction, self.speed, dt)

        if self.rect.left > config.GAME_WINDOW_WIDTH or self.rect.right < 0 or self.rect.top > config.GAME_WINDOW_HEIGHT or self.rect.bottom < 0:
            self.kill()
            
    def set_image(self, file_name):
        image = load_image(config.IMAGEFILE_PATH + file_name + ".png")# 1. Load the original image

        current_angle = calculate_angle_vec_to_degrees_rotate(self.direction) + 180.0 # Angle in degrees
        
        rotated_shell_image = pygame.transform.rotate(image, current_angle)# 2. Rotate the original image

        return rotated_shell_image