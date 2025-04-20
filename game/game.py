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

        self.tankBody_image_original = pygame.image.load("tankBody.png")
        self.scaled_tankBody_image = pygame.transform.smoothscale(self.tankBody_image_original, (50,50))
        self.tankBody_image = self.scaled_tankBody_image.convert_alpha()

        self.turretBody_image_original = pygame.image.load("turretBody.png")
        self.scaled_turretBody_image = pygame.transform.smoothscale(self.turretBody_image_original, (50,50))
        self.turretBody_image = self.scaled_turretBody_image.convert_alpha()

        self.player = Player(100, 100, self.tankBody_image)  
        self.playerRect = self.player.getPlayerRect()



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
        #self.player.draw(self.screen)  
        self.screen.blit(self.tankBody_image, self.playerRect)
        self.screen.blit(self.turretBody_image, self.playerRect)
        pygame.display.flip()