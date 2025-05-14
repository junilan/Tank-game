import pygame

class Unit(pygame.sprite.Sprite):
    '''
    Base class for all units in the game.
    
    Attributes:
        rotaion_speed (float): The speed of rotation.
        direction (pygame.math.Vector2): The direction of the unit.
        speed (float): The speed of the unit.
        tank_speed (float): The speed of the tank.
        health (int): The health of the unit.
        is_alive (bool): Whether the unit is alive or not.
    '''
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
        # This method is called when the unit takes damage.
        self.health -= damage
        print(f"health: {self.health}")
        if self.health <= 0:
            self.kill()
            self.is_alive = False

            