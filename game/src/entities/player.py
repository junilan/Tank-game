import pygame
from .character_stats import playerStatus
import config
from .parts import TankBody
from .parts import Turret
from .parts.projectile.shell import Shell
from .parts.projectile.bullet import Bullet
from .tank_unit import TankUnit

from src.utils import load_image

class Player(TankUnit):
    def __init__(self, x, y):
        super().__init__(x, y)

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
        self.rect = self.tank_body.rect

        self.rotaion_speed = playerStatus["rotation_speed"]
        self.direction = pygame.math.Vector2(playerStatus["init_direction"])
        self.speed = 0
        self.tank_speed = playerStatus["speed"]
        
        self.is_fired_shell = False
        self.shell = Shell(x, y, self.direction)
        self.shell_group = pygame.sprite.Group()
        
        self.is_fired_bullet = False
        self.bullet = Bullet(x, y, self.direction)
        self.Bullet_group = pygame.sprite.Group()

        self.cooldown = 0

    def update(self, dt):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # Rotate the tank left
            self.tank_body.rotate(-self.rotaion_speed)
        if keys[pygame.K_d]: # Rotate the tank right
            self.tank_body.rotate(+self.rotaion_speed)

        if keys[pygame.K_w]: # Move the tank forward
            self.tank_body.move(self.tank_speed)
        elif keys[pygame.K_s]: # Move the tank backward
            self.tank_body.move(-self.tank_speed)
        else: # Stop the tank
            self.tank_body.move(0)

        mouse_click = pygame.mouse.get_pressed()

        if mouse_click[0]:
            # Fire the main cannon
            self.fire_shell()
        if mouse_click[2]:
            # Fire the main cannon
            self.fire_bullet()
            
        self.tank_body.update(dt)
        self.rect = self.tank_body.rect

        # Update turret position
        self.turret.update(self.tank_body.rect.centerx, self.tank_body.rect.centery)

        self.shell_group.update(dt)
        self.Bullet_group.update(dt)

        
        if self.is_fired_shell == True:
            self.cooldown += 1 * dt
            if self.cooldown >= playerStatus["cannon_attack_speed"]: 
                self.cooldown = 0
                self.is_fired_shell = False

        if self.is_fired_bullet == True:
            self.cooldown += 1 * dt
            if self.cooldown >= playerStatus["machine_gun_attack_speed"]: 
                self.cooldown = 0
                self.is_fired_bullet = False

        


    def draw(self, screen):
        self.tank_body.draw(screen)
        self.turret.draw(screen)
        self.shell_group.draw(screen)
        self.Bullet_group.draw(screen)

    def fire_shell(self):
        # Implement firing logic for the main cannon here
        if self.is_fired_shell == False:
            self.is_fired_shell = True
            offset_shell = pygame.Vector2(0, -self.turret.shell_fired_pos)  # Offset position to relocate cannon body's pivot point
            turret_angle = self.turret.direction.angle_to(pygame.Vector2(0, 1)) - 180.0
            rotated_offset_shell = offset_shell.rotate(-turret_angle)# Offset rotating for cannon body's pivot point
            shell_pos = pygame.Vector2((self.turret.x, self.turret.y) + rotated_offset_shell)
            shell = Shell(shell_pos.x, shell_pos.y, self.turret.direction)
            self.shell_group.add(shell)

    def fire_bullet(self):
        # Implement firing logic for the sub machine gun here
        if self.is_fired_bullet == False:
            self.is_fired_bullet = True
            offset_bullet = pygame.Vector2(-self.tank_body.bullet_fired_pos_x, self.tank_body.bullet_fired_pos_y)  # Offset position to relocate cannon body's pivot point
            turret_angle = self.tank_body.direction.angle_to(pygame.Vector2(0, 1)) - 180.0
            #print(turret_angle)
            rotated_offset_bullet = offset_bullet.rotate(-turret_angle)# Offset rotating for cannon body's pivot point
            bullet_pos = pygame.Vector2((self.tank_body.rect.centerx, self.tank_body.rect.centery) + rotated_offset_bullet)
            bullet = Bullet(bullet_pos.x, bullet_pos.y, self.tank_body.direction)
            self.Bullet_group.add(bullet)

            
