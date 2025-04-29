import pygame
import math
import config
from entities import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("My Pygame Project")
        self.clock = pygame.time.Clock()
        self.running = True

        image_add = {
            "tankBody": "game/assets/image/tankBody.png",
            "turretBody": "game/assets/image/turretBody.png",
            "cannonCover": "game/assets/image/cannonCover.png",
            "cannonBody": "game/assets/image/cannon.png",
        }
        self.player = Player(config.WIDTH/2, config.HEIGHT-100, image_add)  



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

    def draw(self):
        self.screen.fill((30, 30, 30)) 

        self.player.draw(self.screen)  
        
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()