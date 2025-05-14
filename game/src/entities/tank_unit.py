import pygame
from .unit import Unit
from .parts.projectile.shell import Shell
from .parts.projectile.bullet import Bullet
from .parts import TankBody
from .parts import Turret

class TankUnit(Unit):
    '''
    Base class for all tank units in the game.

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
        
        self.speed = 0
        self.is_fired_shell = False
        self.shell_group = pygame.sprite.Group()
        
        self.is_fired_bullet = False
        self.Bullet_group = pygame.sprite.Group()

    def update(self, dt):
        if self.is_alive:
            self.tank_body.update(dt)
            self.rect = self.tank_body.rect

            # Update turret position
            self.turret.update(self.tank_body.rect.centerx, self.tank_body.rect.centery)

            self.shell_group.update(dt)
            self.Bullet_group.update(dt)

        


    def draw(self, screen):
        pass

    def set_attributes(self, tank_body_image_file, turret_image_files, STATUS, x, y):
        # Initialize the tank body and turret with the given images and status

        self.tank_body = TankBody(x, y, tank_body_image_file)
        self.turret = Turret(x, y, turret_image_files)
        self.tank_body_group = pygame.sprite.GroupSingle(self.tank_body)
        self.turret_group = pygame.sprite.GroupSingle(self.turret)
        self.rect = self.tank_body.rect
        self.image = self.tank_body.image
        self.mask = self.tank_body.mask

        self.rotaion_speed = STATUS["rotation_speed"]
        self.direction = pygame.math.Vector2(STATUS["init_direction"])
        self.tank_speed = STATUS["speed"]
        self.cannon_attack_speed = STATUS["cannon_attack_speed"]
        self.machine_gun_attack_speed = STATUS["machine_gun_attack_speed"]

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

    def reloading(self, is_fired, cooldown_cnt, cooldown_time, dt):
        # Reloading logic for the tank unit
        if is_fired == True:
            cooldown_cnt += 1 * dt
            if cooldown_cnt >= cooldown_time: 
                cooldown_cnt = 0
                is_fired = False

        return is_fired, cooldown_cnt

    def take_damage(self, damage):
        # This method is called when the unit takes damage.
        self.health -= damage
        print(f"health: {self.health}")
        if self.health <= 0:
            self.is_alive = False
            print("killed!")
            self.kill()
            self.tank_body.kill()
            self.turret.kill()
            self.Bullet_group.empty()
            self.shell_group.empty()
            
