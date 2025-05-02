import pygame
from src.entities.character_stats import playerStatus

class TankBody:
    def __init__(self, x, y, image_file):

        self.x = x
        self.y = y

        self.image_files = {
            "tank_body": image_file["tank_body"],
        }

        self.rect = self.image_files["tank_body"].get_rect() 
        self.rect.center = (x, y)

        self.direction = pygame.math.Vector2(playerStatus["init_direction"])
        self.speed = 0
        self.rotaion_speed = playerStatus["rotation_speed"]
        self.tank_speed = playerStatus["speed"]

    def update(self, dt):
        self.dt = dt
        current_center_pos = pygame.Vector2(self.rect.center)
        current_angle = self.direction.angle_to(pygame.Vector2(0, 1))  # Angle in degrees

        # 2. Rotate the original image
        self.rotated_body_image = pygame.transform.rotate(self.image_files["tank_body"], -current_angle)

        # 3. Get the rect of the rotated image and position it
        self.rotated_rect = self.rotated_body_image.get_rect(center = current_center_pos)

    def draw(self, screen):

        screen.blit(self.rotated_body_image, self.rotated_rect)

        #pygame.draw.circle(screen, (0, 255, 0), current_center_pos, 5, 0)
        #pygame.draw.circle(screen, (255, 255, 0), current_center_turret_pos, 5, 0)

    def rotate(self, angle_degrees):
        self.direction = self.direction.rotate(angle_degrees)

    def move(self, speed):
        self.speed = speed

        if self.speed != 0:
            movement = self.direction * self.speed * self.dt
            self.x += movement.x
            self.y -= movement.y
            self.rect.center = (int(self.x), int(self.y))