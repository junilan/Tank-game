import pygame
from .character_stats import ENEMYSTATUS
import config
from .parts import TankBody
from .parts import Turret
from .parts.projectile.shell import Shell
from .parts.projectile.bullet import Bullet
from .tank_unit import TankUnit

from src.utils import load_image

class EnemyTank(TankUnit):
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
        
        self.set_attributes(tank_body_image_file, turret_image_files, ENEMYSTATUS, x, y)
        self.cooldown_cnt_shell = 0
        self.cooldown_cnt_bullet = 0

    def update(self, dt, player_x, player_y):

        aim_pos_x, aim_pos_y = player_x, player_y
        self.turret.rotate(aim_pos_x, aim_pos_y)

        self.fire_shell()
        self.is_fired_shell, self.cooldown_cnt_shell = self.reloading(self.is_fired_shell, self.cooldown_cnt_shell, self.cannon_attack_speed, dt)
        #self.is_fired_bullet, self.cooldown_cnt_bullet = self.reloading(self.is_fired_bullet, self.cooldown_cnt_bullet, self.machine_gun_attack_speed, dt)


        super().update(dt)

       
