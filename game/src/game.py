import pygame
import math
import config
import random
from src.entities import Player
from src.entities import EnemyDummy
from src.entities import EnemyTank

class Game:
    '''
    Main game class that initializes the game, handles events, updates game state, and draws the game objects.
    '''
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.GAME_WINDOW_WIDTH, config.GAME_WINDOW_HEIGHT))
        pygame.display.set_caption("My Pygame Project")
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(config.GAME_WINDOW_WIDTH/2, config.GAME_WINDOW_HEIGHT-100)  
        self.player_group = pygame.sprite.Group(self.player)
        self.player_sprite_group = pygame.sprite.Group(self.player.tank_body, self.player.turret)
        
        self.enemy_tank = EnemyTank(config.GAME_WINDOW_WIDTH/2, 100)
        self.enemy_tank_group = pygame.sprite.Group(self.enemy_tank)
        self.enemy_tank_sprite_group = pygame.sprite.Group(self.enemy_tank.tank_body, self.enemy_tank.turret)

        self.enemy_dummy_group = pygame.sprite.Group() 
        for _ in range(10):
            enemy = EnemyDummy(0, 0)
            while True:
                enemy.rect.x = random.randint(0, config.GAME_WINDOW_WIDTH - enemy.rect.width)
                enemy.rect.y = random.randint(0, config.GAME_WINDOW_HEIGHT - enemy.rect.height)
                if not pygame.sprite.spritecollide(enemy, self.enemy_dummy_group, False):
                    self.enemy_dummy_group.add(enemy)
                    break
        



    def run(self):
        while self.running:
            self.dt = self.clock.tick(config.FPS) / 1000.0
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        #self.player.update(self.dt)
        self.player_group.update(self.dt)
        self.enemy_dummy_group.update(self.dt)
        self.enemy_tank_group.update(self.dt, self.player.rect.centerx, self.player.rect.centery)

        '''
        Temporary collision detection and handling(will be organized this code later)
        '''
        collisions_by_player = pygame.sprite.groupcollide(self.player_group, self.enemy_dummy_group, False, False)
        for players, enemies in collisions_by_player.items():
            for enemy in enemies:
                enemy.take_damage(100)   
        collisions_player_ememy_tanks = pygame.sprite.groupcollide(self.player_group, self.enemy_tank_group, False, False)
        for player, enemies in collisions_player_ememy_tanks.items():
            for enemy in enemies:
                enemy.speed = 0
                player.tank_speed = 0

        collisions_by_enemy_to_player_with_shell = pygame.sprite.groupcollide(self.enemy_tank.shell_group, self.player_group, True, False, pygame.sprite.collide_mask)
        for bullet, players in collisions_by_enemy_to_player_with_shell.items():
            for player in players:
                player.take_damage(50)   
        
        collisions_by_player_to_enemy_dummy_with_bullet = pygame.sprite.groupcollide(self.player.Bullet_group, self.enemy_dummy_group, True, False, pygame.sprite.collide_mask)
        for bullet, enemies in collisions_by_player_to_enemy_dummy_with_bullet.items():
            for enemy in enemies:
                enemy.take_damage(10)
        collisions_by_player_to_enemy_dummy_with_bullet = pygame.sprite.groupcollide(self.player.shell_group, self.enemy_dummy_group, True, False, pygame.sprite.collide_mask)
        for shell, enemies in collisions_by_player_to_enemy_dummy_with_bullet.items():
            for enemy in enemies:
                enemy.take_damage(50)

        collisions_by_player_to_enemy_with_bullet = pygame.sprite.groupcollide(self.player.Bullet_group, self.enemy_tank_group, True, False, pygame.sprite.collide_mask)
        for bullet, enemies in collisions_by_player_to_enemy_with_bullet.items():
            for enemy in enemies:
                enemy.take_damage(0)
        collisions_by_player_to_enemy_with_shell = pygame.sprite.groupcollide(self.player.shell_group, self.enemy_tank_group, True, False, pygame.sprite.collide_mask)
        for shell, enemies in collisions_by_player_to_enemy_with_shell.items():
            for enemy in enemies:
                enemy.take_damage(50)
            

    def draw(self):
        self.screen.fill((60, 60, 0)) 

        #self.player.draw(self.screen)  
        self.player_sprite_group.draw(self.screen)
        self.player.Bullet_group.draw(self.screen)
        self.player.shell_group.draw(self.screen)
        self.enemy_dummy_group.draw(self.screen)
        self.enemy_tank_sprite_group.draw(self.screen)
        self.enemy_tank.shell_group.draw(self.screen)
        self.enemy_tank.Bullet_group.draw(self.screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()