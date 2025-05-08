import pygame
from src.entities.character_stats import PLAYERSTATUS
from src.entities.parts.projectile.shell import Shell
from src.entities.parts.projectile.bullet import Bullet
from src.utils import calculate_angle_vec_to_degrees_rotate


class Turret(pygame.sprite.Sprite):
    def __init__(self, x, y, image_files):
        super().__init__()
        self.x = x
        self.y = y

        self.image_files = {
            "turret_body": image_files["turret_body"],
            "cannon_cover": image_files["cannon_cover"],
            "cannon_body": image_files["cannon_body"],
        }
        
        self.rotaion_speed = PLAYERSTATUS["rotation_speed"]
        self.direction = pygame.math.Vector2(PLAYERSTATUS["init_direction"])

        self.cannon_pos = (image_files["cannon_cover"].get_height() / 2) / 5
        self.shell_fired_pos = (image_files["cannon_body"].get_height() / 2) + self.cannon_pos

    def update(self, x, y):
        self.x = x
        self.y = y
        current_turret_pos = pygame.Vector2(self.x, self.y)
        self.direction = self.aim_pos_vector - current_turret_pos

        if self.direction.length() > 0: self.direction = self.direction.normalize()

        turret_angle = calculate_angle_vec_to_degrees_rotate(self.direction)  # Angle in degrees
        current_center_turret_pos = current_turret_pos


        self.rotated_turretBody_image = pygame.transform.rotate(self.image_files["turret_body"], turret_angle)
        self.rotated_cannonCover_image = pygame.transform.rotate(self.image_files["cannon_cover"], turret_angle)
        self.rotated_cannonBody_image = pygame.transform.rotate(self.image_files["cannon_body"], turret_angle)

        offset_cannonBody = pygame.Vector2(0, -self.cannon_pos)  # Offset position to relocate cannon body's pivot point
        rotated_offset_cannonBody = offset_cannonBody.rotate(-turret_angle)# Offset rotating for cannon body's pivot point
        
        self.rotated_rect_turretBody = self.rotated_turretBody_image.get_rect(center = current_center_turret_pos)
        self.rotated_rect_cannonCover = self.rotated_cannonCover_image.get_rect(center = current_center_turret_pos)
        self.rotated_rect_cannonBody = self.rotated_cannonBody_image.get_rect(center = current_center_turret_pos + rotated_offset_cannonBody)
        
    def draw(self, screen):
        screen.blit(self.rotated_turretBody_image, self.rotated_rect_turretBody)
        screen.blit(self.rotated_cannonBody_image, self.rotated_rect_cannonBody)
        screen.blit(self.rotated_cannonCover_image, self.rotated_rect_cannonCover)
        
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 5, 0)

    def rotate(self, x, y):
        self.aim_pos_vector = pygame.Vector2(x, y)

    def cannon_moving(self):
        pass

            

