import pygame
from .character_stats import playerStatus
import config
from .parts import TankBody
from .parts import Turret

from src.utils import load_image

class Player:
    def __init__(self, x, y):
        tank_body_image_file = {
            "tank_body": load_image(config.IMAGEFILE_PATH + "tankBody.png"),
        }
        turret_image_files = {
            "turret_body": load_image(config.IMAGEFILE_PATH + "turretBody.png"),
            "cannon_cover": load_image(config.IMAGEFILE_PATH + "cannonCover.png"),
            "cannon_body": load_image(config.IMAGEFILE_PATH + "cannon.png"),
        }
        
        self.tank_body = TankBody(x, y, tank_body_image_file)
        self.turret = Turret(x, y, turret_image_files)

        self.rotaion_speed = playerStatus["rotation_speed"]
        self.direction = pygame.math.Vector2(playerStatus["init_direction"])
        self.speed = 0
        self.tank_speed = playerStatus["speed"]


    def update(self, dt):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # Rotate the tank left
            self.tank_body.rotate(+self.rotaion_speed)
        if keys[pygame.K_d]: # Rotate the tank right
            self.tank_body.rotate(-self.rotaion_speed)

        if keys[pygame.K_w]: # Move the tank forward
            self.tank_body.move(self.tank_speed)
        elif keys[pygame.K_s]: # Move the tank backward
            self.tank_body.move(-self.tank_speed)
        else: # Stop the tank
            self.tank_body.move(0)

        mouse_click = pygame.mouse.get_pressed()

        if mouse_click[0]:
            # Fire the main cannon
            self.turret.fire_shell(self.tank_body.x, self.tank_body.y)
            
        if keys[pygame.K_SPACE]:
            if self.turret.is_fired_shell:
                self.turret.is_fired_shell = False

        self.tank_body.update(dt)

        # Update turret position
        self.turret.update(self.tank_body.x, self.tank_body.y)


    def draw(self, screen):
        self.tank_body.draw(screen)
        self.turret.draw(screen)

            
