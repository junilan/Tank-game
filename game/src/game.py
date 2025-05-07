import pygame
import math
import config
from src.entities import Player
from src.entities import EnemyDummy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.GAME_WINDOW_WIDTH, config.GAME_WINDOW_HEIGHT))
        pygame.display.set_caption("My Pygame Project")
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(config.GAME_WINDOW_WIDTH/2, config.GAME_WINDOW_HEIGHT-100)  
        self.enemy = EnemyDummy(config.GAME_WINDOW_WIDTH/2, 100)
        self.enemy_group = pygame.sprite.Group(self.enemy) 



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
        self.enemy.update(self.dt)

        if pygame.sprite.spritecollide(self.player, self.enemy_group, False):
            print("Collision detected!")
        
        collisions = pygame.sprite.groupcollide(self.player.Bullet_group, self.enemy_group, False, False)
        for projectile, hit_enemies in collisions.items():
            print(f"Projectile {projectile} hit enemies: {hit_enemies}")


    def draw(self):
        self.screen.fill((60, 60, 0)) 

        self.player.draw(self.screen)  
        self.enemy.draw(self.screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()