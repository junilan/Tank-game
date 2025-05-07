import pygame

class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rotaion_speed = 0
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0
        self.tank_speed = 0

    def update(self, dt):
        pass

    def draw(self, screen):
        pass
