import pygame
from src.utils import calculate_angle_vec_to_degrees_rotate, movement_vector
from src.entities.character_stats import PLAYERSTATUS

class TankBody(pygame.sprite.Sprite):
    '''
    TankBody class that represents the body of a tank.

    Attributes:
        direction (pygame.math.Vector2): The direction the tank is facing.
        speed (float): The speed of the tank.
        rotaion_speed (float): The speed of rotation.
        tank_speed (float): The speed of the tank.
        image_files (dict): Dictionary containing image files for the tank body.
        rotated_body_image (pygame.Surface): The rotated image of the tank body.
        rect (pygame.Rect): The rectangle representing the tank's position and size.
        mask (pygame.mask.Mask): The mask for collision detection.
        bullet_fired_pos_x (float): The x-coordinate where bullets are fired from.
        bullet_fired_pos_y (float): The y-coordinate where bullets are fired from.
    '''
    def __init__(self, x, y, image_file):
        super().__init__()

        self.direction = pygame.math.Vector2(PLAYERSTATUS["init_direction"])
        self.speed = 0
        self.rotaion_speed = PLAYERSTATUS["rotation_speed"]
        self.tank_speed = PLAYERSTATUS["speed"]

        self.image_files = {
            "tank_body": image_file["tank_body"],
        }
        
        current_angle = calculate_angle_vec_to_degrees_rotate(self.direction)  # Angle in degrees
        

        # 2. Rotate the original image
        self.rotated_body_image = pygame.transform.rotate(self.image_files["tank_body"], current_angle)
        
        self.image = self.rotated_body_image
        # 3. Get the rect of the rotated image and position it
        self.rect = self.rotated_body_image.get_rect(center = (x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.bullet_fired_pos_x = (self.image_files["tank_body"].get_width() / 2) - ((self.image_files["tank_body"].get_width() / 2) / 1.3)
        self.bullet_fired_pos_y = (self.image_files["tank_body"].get_height() / 2) - ((self.image_files["tank_body"].get_height() / 2) / 3)

    def update(self, dt):
        self.dt = dt
        current_center_pos = pygame.Vector2(self.rect.center)
        current_angle = calculate_angle_vec_to_degrees_rotate(self.direction)  # Angle in degrees

        # 2. Rotate the original image
        self.rotated_body_image = pygame.transform.rotate(self.image_files["tank_body"], current_angle)
        
        self.image = self.rotated_body_image
        # 3. Get the rect of the rotated image and position it
        self.rect = self.rotated_body_image.get_rect(center = current_center_pos)
        self.mask = pygame.mask.from_surface(self.image)

    def rotate(self, angle_degrees):
        # Rotate the tank body by a given angle in degrees.
        self.direction = self.direction.rotate(angle_degrees)

    def move(self, speed):
        # Move the tank body in the current direction with a given speed.
        self.speed = speed

        if self.speed != 0:
            self.rect.center = movement_vector(self.rect.centerx, self.rect.centery, self.direction, self.speed, self.dt)