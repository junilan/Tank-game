import pygame
import config

image_cache = {}

def load_image(path):
    """
    Load an image from the specified path and convert it to a format suitable for display.
    """
    if path not in image_cache:
        try:
            image = pygame.image.load(path)
            scaled_image = pygame.transform.smoothscale(image, (config.IMAGESCALE, config.IMAGESCALE))
            image_cache[path] = scaled_image.convert_alpha() 
        except pygame.error as e:
            print(f"fail to load image at {path}: {e}")
            return None

    return image_cache[path]
