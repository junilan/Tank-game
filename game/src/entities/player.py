import pygame
from .character_stats import playerStatus

class Player:
    def __init__(self, x, y, player_image):
        self.tank_body_image = self.imageLoad(player_image["tankBody"])
        self.turret_body_image = self.imageLoad(player_image["turretBody"])
        self.cannon_cover_image = self.imageLoad(player_image["cannonCover"])
        self.cannon_body_image = self.imageLoad(player_image["cannonBody"])

        self.rect = self.tank_body_image.get_rect() 
        self.rect.center = (x, y)
        self.color = (0, 255, 0)
        #self.speed = playerStatus["speed"]
        self.angle = 90.0
        self.turningSpeed = 2.0

        self.x = x
        self.y = y
        self.direction = pygame.math.Vector2(0, 1)
        self.speed = 0
        self.rotaion_speed = 2

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(+self.rotaion_speed)
        if keys[pygame.K_d]:
            self.rotate(-self.rotaion_speed)

        if keys[pygame.K_w]:
            #self.rect.x += self.speed * math.cos(math.radians(self.angle))
            #self.rect.y -= self.speed * math.sin(math.radians(self.angle))
            self.speed = playerStatus["speed"]
        elif keys[pygame.K_s]:
            #self.rect.x -= self.speed * math.cos(math.radians(self.angle))
            #self.rect.y += self.speed * math.sin(math.radians(self.angle))
            self.speed = -playerStatus["speed"]
        else:
            self.speed = 0

        if self.speed != 0:
            movement = self.direction * self.speed * dt
            self.x += movement.x
            self.y -= movement.y
            self.rect.center = (int(self.x), int(self.y))


    def draw(self, screen):
        current_center_pos = pygame.Vector2(self.rect.center)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos_vector = pygame.Vector2(mouse_x, mouse_y)
        turret_direction = mouse_pos_vector - current_center_pos
        offset_cannonBody = pygame.Vector2(0, -10)  # Offset position to relocate cannon body's pivot point

        if turret_direction.length() > 0: 
            turret_direction = turret_direction.normalize()

        current_angle = self.direction.angle_to(pygame.Vector2(0, 1))  # Angle in degrees
        turret_angle = turret_direction.angle_to(pygame.Vector2(0, 1)) - 180.0  # Angle in degrees



        current_center_turret_pos = current_center_pos
        original_body_image = self.tank_body_image
        original_turretBody_image = self.turret_body_image 

        # 2. Rotate the original image
        rotated_body_image = pygame.transform.rotate(self.tank_body_image, -current_angle)
        rotated_turretBody_image = pygame.transform.rotate(self.turret_body_image , turret_angle)
        rotated_cannonCover_image = pygame.transform.rotate(self.cannon_cover_image, turret_angle)
        rotated_cannonBody_image = pygame.transform.rotate(self.cannon_body_image , turret_angle)
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
        pygame.draw.circle(screen, (0, 255, 0), current_center_pos, 5, 0)
        pygame.draw.circle(screen, (255, 255, 0), current_center_turret_pos, 5, 0)

    def rotate(self, angle_degrees):
        self.direction = self.direction.rotate(angle_degrees)

    def imageLoad(self, imagePath):
        original_image = pygame.image.load(imagePath)
        scaled_image = pygame.transform.smoothscale(original_image, (100, 100))
        converted_image = scaled_image.convert_alpha()
        return converted_image
