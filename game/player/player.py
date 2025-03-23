import pygame
from .settings_player import playerStatus

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)  
        self.color = (0, 255, 0)
        self.speed = playerStatus["speed"]

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)