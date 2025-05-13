import pygame
from src.utils import calculate_angle_vec_to_degrees_rotate, movement_vector
from src.entities.character_stats import PLAYERSTATUS

class TankBody(pygame.sprite.Sprite):
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
        self.direction = self.direction.rotate(angle_degrees)

    def move(self, speed):
        '''Move the tank body in the direction it is facing.'''
        self.speed = speed

        if self.speed != 0:
            self.rect.center = movement_vector(self.rect.centerx, self.rect.centery, self.direction, self.speed, self.dt)