import pygame
from .base_scene import BaseScene

class GameScene(BaseScene):
    def __init__(self, manager):
        super().__init__(manager)
        self.player = pygame.Rect(350, 250, 50, 50)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.manager.change_scene("menu")  

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.x -= 5
        if keys[pygame.K_RIGHT]:
            self.player.x += 5
        if keys[pygame.K_UP]:
            self.player.y -= 5
        if keys[pygame.K_DOWN]:
            self.player.y += 5

    def draw(self):
        self.manager.screen.fill((30, 30, 30))
        pygame.draw.rect(self.manager.screen, (0, 255, 0), self.player)