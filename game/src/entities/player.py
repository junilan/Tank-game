import pygame
from .character_stats import playerStatus
import config
from .parts import TankBody
from .parts import Turret

from src.utils import load_image

class Player:
    def __init__(self, x, y):
        #self.tank_body_image_file = load_image(config.IMAGEFILE_PATH + "tankBody.png")
        turret_image_files = {
            "tank_body": load_image(config.IMAGEFILE_PATH + "tankBody.png"),
            "turret_body": load_image(config.IMAGEFILE_PATH + "turretBody.png"),
            "cannon_cover": load_image(config.IMAGEFILE_PATH + "cannonCover.png"),
            "cannon_body": load_image(config.IMAGEFILE_PATH + "cannon.png"),
        }

        self.tank_body = TankBody(x, y, turret_image_files)

    def update(self, dt):
        self.tank_body.update(dt)

    def draw(self, screen):
        self.tank_body.draw(screen)