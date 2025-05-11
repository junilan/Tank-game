import pygame
import math
from src.entities.character_stats import PLAYERSTATUS
from src.utils import calculate_angle_vec_to_degrees_rotate

class Turret(pygame.sprite.Sprite):
    def __init__(self, x, y, image_files):
        super().__init__()
        self.x = x
        self.y = y

        self.cannon_pos = (image_files["cannon_cover"].get_height() / 2) / 5
        self.shell_fired_pos = (image_files["cannon_body"].get_height() / 2) + self.cannon_pos

        self.original_image = self.combine_images(image_files)

        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = pygame.math.Vector2(PLAYERSTATUS["init_direction"])
        self.angle = 0

    def combine_images(self, image_files):

        turret_body_image = image_files["turret_body"]
        cannon_cover_image = image_files["cannon_cover"]
        cannon_body_image = image_files["cannon_body"]

        width = max(turret_body_image.get_width(), cannon_cover_image.get_width(), cannon_body_image.get_width())
        height = turret_body_image.get_height() + max(cannon_cover_image.get_height(), cannon_body_image.get_height())

        combined_image = pygame.Surface((width, height), pygame.SRCALPHA)

        combined_image.blit(turret_body_image, (0, turret_body_image.get_height()/2))
        combined_image.blit(cannon_body_image, (0, cannon_body_image.get_height()/2 - self.cannon_pos))
        combined_image.blit(cannon_cover_image, (0, cannon_cover_image.get_height()/2))

        return combined_image

    def update(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (x, y) 
        self.direction = self.aim_pos_vector - pygame.Vector2(self.x, self.y)
        if self.direction.length() > 0:
            self.direction.normalize_ip()

        self.angle = math.degrees(math.atan2(-self.direction.y, self.direction.x)) - 90

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y)) 

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 5, 0)

    def rotate(self, x, y):
        self.aim_pos_vector = pygame.Vector2(x, y)