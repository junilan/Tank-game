#from game import Game

#if __name__ == "__main__":
#    game = Game()
#    game.run()

import pygame
from game.scene_manager import SceneManager
from game.scenes.menu import MenuScene
from game.scenes.game_play import GameScene

# 
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 
manager = SceneManager("menu")
manager.screen = screen

# 
manager.add_scene("menu", MenuScene(manager))
manager.add_scene("gameplay", GameScene(manager))
manager.change_scene("menu")

# 
manager.run()

pygame.quit()