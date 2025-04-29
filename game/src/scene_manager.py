import pygame

class SceneManager:
    def __init__(self, start_scene):
        self.scenes = {}  
        self.current_scene = None
        self.running = True
        self.clock = pygame.time.Clock()
        #self.change_scene(start_scene)

    def add_scene(self, name, scene):
       
        self.scenes[name] = scene

    def change_scene(self, name):
       
        if name in self.scenes:
            self.current_scene = self.scenes[name]
            self.current_scene.start()

    def run(self):
        
        while self.running:
            
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.current_scene.handle_events(event)
            
            self.current_scene.update()
            self.current_scene.draw()
            pygame.display.flip()