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

    def update(self, x, y):
        self.x = x
        self.y = y
        current_tank_body_pos = pygame.Vector2(self.x, self.y)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos_vector = pygame.Vector2(mouse_x, mouse_y)
        turret_direction = mouse_pos_vector - current_tank_body_pos

        offset_cannonBody = pygame.Vector2(0, -10)  # Offset position to relocate cannon body's pivot point

        if turret_direction.length() > 0: turret_direction = turret_direction.normalize()

        turret_angle = turret_direction.angle_to(pygame.Vector2(0, 1)) - 180.0  # Angle in degrees
        current_center_turret_pos = current_tank_body_pos

        self.rotated_turretBody_image = pygame.transform.rotate(self.image_files["turret_body"], turret_angle)
        self.rotated_cannonCover_image = pygame.transform.rotate(self.image_files["cannon_cover"], turret_angle)
        self.rotated_cannonBody_image = pygame.transform.rotate(self.image_files["cannon_body"], turret_angle)
        rotated_offset_cannonBody = offset_cannonBody.rotate(-turret_angle)# Offset rotating for cannon body's pivot point
        
        self.rotated_rect_turretBody = self.rotated_turretBody_image.get_rect(center = current_center_turret_pos)
        self.rotated_rect_cannonCover = self.rotated_cannonCover_image.get_rect(center = current_center_turret_pos)
        self.rotated_rect_cannonBody = self.rotated_cannonBody_image.get_rect(center = current_center_turret_pos + rotated_offset_cannonBody)

    def draw(self, screen):
        screen.blit(self.rotated_turretBody_image, self.rotated_rect_turretBody)
        screen.blit(self.rotated_cannonBody_image, self.rotated_rect_cannonBody)
        screen.blit(self.rotated_cannonCover_image, self.rotated_rect_cannonCover)

    def fire(self):
        # Implement firing logic here
        pass