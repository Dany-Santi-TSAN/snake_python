import pygame
import random

class Food:
    def __init__(self):
        self.spawn()
        self.color = (0, 0, 0)  # Dark color

    def spawn(self):
        # Random spawn within the 600x600 screen limit
        self.position = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
        print(f"Food spawned at: {self.position}")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], 10, 10))
