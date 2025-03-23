import pygame
from .base_scene import BaseScene

class MenuScene(BaseScene):
    def __init__(self, manager):
        super().__init__(manager)
        self.font = pygame.font.Font(None, 40)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.manager.change_scene("gameplay")  

    def draw(self):
        self.manager.screen.fill((0, 0, 0))
        text = self.font.render("Press ENTER to Start", True, (255, 255, 255))
        self.manager.screen.blit(text, (200, 250))