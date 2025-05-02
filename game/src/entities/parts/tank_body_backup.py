import pygame
from src.entities.character_stats import playerStatus

class TankBody:
    def __init__(self, x, y, image_file):

        self.x = x
        self.y = y

        self.image_files = {
            "tank_body": image_file["tank_body"],
            "turret_body": image_file["turret_body"],
            "cannon_cover": image_file["cannon_cover"],
            "cannon_body": image_file["cannon_body"],
        }

        self.rect = image_file["tank_body"].get_rect() 
        self.rect.center = (x, y)

        self.direction = pygame.math.Vector2(playerStatus["init_direction"])
        self.speed = 0
        self.rotaion_speed = playerStatus["rotation_speed"]
        self.tank_speed = playerStatus["speed"]

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(+self.rotaion_speed)
        if keys[pygame.K_d]:
            self.rotate(-self.rotaion_speed)

        if keys[pygame.K_w]:
            #self.rect.x += self.speed * math.cos(math.radians(self.angle))
            #self.rect.y -= self.speed * math.sin(math.radians(self.angle))
            self.speed = self.tank_speed
        elif keys[pygame.K_s]:
            #self.rect.x -= self.speed * math.cos(math.radians(self.angle))
            #self.rect.y += self.speed * math.sin(math.radians(self.angle))
            self.speed = -self.tank_speed
        else:
            self.speed = 0

        if self.speed != 0:
            movement = self.direction * self.speed * dt
            self.x += movement.x
            self.y -= movement.y
            self.rect.center = (int(self.x), int(self.y))


    def draw(self, screen):
        current_center_pos = pygame.Vector2(self.rect.center)
        current_angle = self.direction.angle_to(pygame.Vector2(0, 1))  # Angle in degrees

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos_vector = pygame.Vector2(mouse_x, mouse_y)
        turret_direction = mouse_pos_vector - current_center_pos

        offset_cannonBody = pygame.Vector2(0, -10)  # Offset position to relocate cannon body's pivot point

        if turret_direction.length() > 0: turret_direction = turret_direction.normalize()

        turret_angle = turret_direction.angle_to(pygame.Vector2(0, 1)) - 180.0  # Angle in degrees
        current_center_turret_pos = current_center_pos

        # 2. Rotate the original image
        rotated_body_image = pygame.transform.rotate(self.image_files["tank_body"], -current_angle)
        rotated_turretBody_image = pygame.transform.rotate(self.image_files["turret_body"], turret_angle)
        rotated_cannonCover_image = pygame.transform.rotate(self.image_files["cannon_cover"], turret_angle)
        rotated_cannonBody_image = pygame.transform.rotate(self.image_files["cannon_body"], turret_angle)
        rotated_offset_cannonBody = offset_cannonBody.rotate(-turret_angle)# Offset rotating for cannon body's pivot point

        # 3. Get the rect of the rotated image and position it
        rotated_rect = rotated_body_image.get_rect(center = current_center_pos)
        rotated_rect_turretBody = rotated_turretBody_image.get_rect(center = current_center_turret_pos)
        rotated_rect_cannonCover = rotated_cannonCover_image.get_rect(center = current_center_turret_pos)
        rotated_rect_cannonBody = rotated_cannonBody_image.get_rect(center = current_center_turret_pos + rotated_offset_cannonBody)

        screen.blit(rotated_body_image, rotated_rect)
        screen.blit(rotated_turretBody_image, rotated_rect_turretBody)
        screen.blit(rotated_cannonBody_image, rotated_rect_cannonBody)
        screen.blit(rotated_cannonCover_image, rotated_rect_cannonCover)

        #pygame.draw.circle(screen, (0, 255, 0), current_center_pos, 5, 0)
        #pygame.draw.circle(screen, (255, 255, 0), current_center_turret_pos, 5, 0)

    def rotate(self, angle_degrees):
        self.direction = self.direction.rotate(angle_degrees)