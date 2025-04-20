import pygame
from .settings_player import playerStatus

class Player:
    def __init__(self, x, y, player_image):
        self.rect = player_image.get_rect() 
        self.rect.center = (x, y)
        self.color = (0, 255, 0)
        self.speed = playerStatus["speed"]
        self.angle = 0.5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def getPlayerRect(self):
        return self.rect