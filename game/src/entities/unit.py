import pygame

class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rotaion_speed = 0
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0
        self.tank_speed = 0
        self.health = 100
        self.is_alive = True

    def update(self, dt):
        pass

    def draw(self, screen):
        pass

    def take_damage(self, damage):
        self.health -= damage
        print(f"health: {self.health}")
        if self.health <= 0:
            self.kill()
            self.is_alive = False

            