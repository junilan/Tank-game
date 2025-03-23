import pygame
from .settings import WIDTH, HEIGHT, FPS
from game.player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My Pygame Project")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(100, 100)  

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill((30, 30, 30)) 
        self.player.draw(self.screen)  
        pygame.display.flip()