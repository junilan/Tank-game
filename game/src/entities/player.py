import pygame
from .character_stats import PLAYERSTATUS
import config
from .parts import TankBody
from .parts import Turret
from .parts.projectile.shell import Shell
from .parts.projectile.bullet import Bullet
from .tank_unit import TankUnit

from src.utils import load_image

class Player(TankUnit):
    '''
    Player Tank class that inherits from TankUnit.

    attributes:
        tank_body (TankBody): The body of the tank.
        turret (Turret): The turret of the tank.
        shell_group (pygame.sprite.Group): Group for shells fired from the tank.
        Bullet_group (pygame.sprite.Group): Group for bullets fired from the tank.
        is_fired_shell (bool): Whether the shell has been fired or not.
        is_fired_bullet (bool): Whether the bullet has been fired or not.
    '''
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
        
        self.set_attributes(tank_body_image_file, turret_image_files, PLAYERSTATUS, x, y)
        self.cooldown_cnt_shell = 0
        self.cooldown_cnt_bullet = 0

    def update(self, dt):
        if self.is_alive:
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

            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.turret.rotate(mouse_x, mouse_y)

            self.is_fired_shell, self.cooldown_cnt_shell = self.reloading(self.is_fired_shell, self.cooldown_cnt_shell, self.cannon_attack_speed, dt)
            self.is_fired_bullet, self.cooldown_cnt_bullet = self.reloading(self.is_fired_bullet, self.cooldown_cnt_bullet, self.machine_gun_attack_speed, dt)

            super().update(dt)
            