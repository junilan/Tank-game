import pygame

class BaseScene:
    def __init__(self, manager):
        self.manager = manager  

    def start(self):
        pass

    def handle_events(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass