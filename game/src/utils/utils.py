import pygame
import config
import random

image_cache = {} # Cache to store loaded images

def load_image(path):
    #Load an image from the specified path and convert it to a format suitable for display.
    global image_cache # Cache to store loaded images
    if path not in image_cache: # Check if the image is already loaded
        try:
            image = pygame.image.load(path)# 1. Load the original image
            scaled_image = pygame.transform.smoothscale(image, (config.IMAGESCALE, config.IMAGESCALE))# 2. Scale the image
            image_cache[path] = scaled_image.convert_alpha() # 3. Convert the image to a format suitable for display
        
        except pygame.error as e:
            print(f"fail to load image at {path}: {e}")
            return None

    return image_cache[path]

def calculate_angle_vec_to_vec(v1, v2):
    #Calculate the angle between two vectors.
    dot_product = v1.dot(v2)
    magnitude_v1 = v1.length()
    magnitude_v2 = v2.length()
    
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0
    cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
    angle = pygame.math.acos(cos_theta)
    
    return angle

def calculate_angle_vec_to_degrees_rotate(v):
    #Calculate the angle of a vector in degrees.
    return v.angle_to(pygame.Vector2(0, 1)) - 180.0

def movement_vector(x, y, direction, speed, dt):
    #Calculate the movement vector based on direction, speed, and delta time.
    movement = direction * speed * dt
    x -= movement.x
    y -= movement.y

    return (int(x), int(y))
