import pygame
import math
import config
import random
from src.entities import Player
from src.entities import EnemyDummy
from src.entities import EnemyTank

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.GAME_WINDOW_WIDTH, config.GAME_WINDOW_HEIGHT))
        pygame.display.set_caption("My Pygame Project")
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(config.GAME_WINDOW_WIDTH/2, config.GAME_WINDOW_HEIGHT-100)  

        self.enemy_dummy_group = pygame.sprite.Group() 
        for _ in range(10):
            enemy = EnemyDummy(0, 0)
            while True:
                enemy.rect.x = random.randint(0, config.GAME_WINDOW_WIDTH - enemy.rect.width)
                enemy.rect.y = random.randint(0, config.GAME_WINDOW_HEIGHT - enemy.rect.height)
                if not pygame.sprite.spritecollide(enemy, self.enemy_dummy_group, False):
                    self.enemy_dummy_group.add(enemy)
                    break
        
        self.enemy_tank = EnemyTank(config.GAME_WINDOW_WIDTH/2, 100)
        self.enemy_tank_group = pygame.sprite.Group(self.enemy_tank)



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
        self.player.update(self.dt)
        self.enemy_dummy_group.update(self.dt)
        self.enemy_tank_group.update(self.dt, self.player.rect.centerx, self.player.rect.centery)

        collisions_by_player =  pygame.sprite.spritecollide(self.player, self.enemy_dummy_group, True)
        for enemy in collisions_by_player:
            print(f"Player collided with enemy: {enemy}")
            enemy.take_damage(100)  # Example damage value
            
        
        collisions = pygame.sprite.groupcollide(self.player.Bullet_group, self.enemy_dummy_group, True, True)
        for bullet, enemies in collisions.items():
            for enemy in enemies:
                enemy.take_damage(10)

        collisions = pygame.sprite.groupcollide(self.player.shell_group, self.enemy_dummy_group, True, True)
        for shell, enemies in collisions.items():
            for enemy in enemies:
                enemy.take_damage(50)

        collisions = pygame.sprite.spritecollide(self.enemy_tank, self.player.Bullet_group, True)
        for bullet in collisions:
            bullet.kill()

        collisions = pygame.sprite.spritecollide(self.enemy_tank, self.player.shell_group, True)
        for shell in collisions:
            shell.kill()
            self.enemy_tank.take_damage(50)

    def draw(self):
        self.screen.fill((60, 60, 0)) 

        self.player.draw(self.screen)  
        self.enemy_dummy_group.draw(self.screen)
        self.enemy_tank.draw(self.screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()