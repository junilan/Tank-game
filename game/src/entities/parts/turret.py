import pygame
from src.entities.character_stats import playerStatus

class Turret:
    def __init__(self, x, y, image_files):
        self.x = x
        self.y = y

        self.image_files = {
            "turret_body": image_files["turret_body"],
            "cannon_cover": image_files["cannon_cover"],
            "cannon_body": image_files["cannon_body"],
        }
        
        self.rotaion_speed = playerStatus["rotation_speed"]
        self.direction = pygame.math.Vector2(playerStatus["init_direction"])

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(+self.rotaion_speed)
        if keys[pygame.K_d]:
            self.rotate(-self.rotaion_speed)
       
    def draw(self, screen):
        pass

    def rotate(self, angle_degrees):
        self.direction = self.direction.rotate(angle_degrees)