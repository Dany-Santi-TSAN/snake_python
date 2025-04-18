import pygame
import random

class Food:
    def __init__(self):
        self.spawn()
        self.image = pygame.image.load("sprite/apple_sprite.png")
        self.image = pygame.transform.scale(self.image, (10, 10))

    def spawn(self):
        # Random spawn within the 600x600 screen limit
        self.position = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
        print(f"Food spawned at: {self.position}")

    def draw(self, screen):
        screen.blit(self.image, self.position)
