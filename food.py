import pygame
import random

class Food:

    def __init__(self):
        # Initialize food position with random coordinates (aligned to a 10px grid)
        self.position = (random.randint(0,79)*10, random.randint(0, 59) * 10)
        self.color = (0,0,0) # Dark color

    def spawn(self):
        # random spawn
        self.position = (random.randint(0, 79) * 10, random.randint(0, 59) * 10)

    def draw(self, screen):
        # Draw the food as an apple on the screen
        # Radius is 10 px
        pygame.draw.circle(screen, self.color, self.position, 10)
