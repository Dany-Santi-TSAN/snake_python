import pygame

class Snake:

    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]  # Initial snake position
        self.direction = (10,0) # kickstart to right

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body = [new_head] + self.body[:-1] # move snake

    def draw(self, screen):
        for segment in self.body:
            # draw each segment
            pygame.draw.rect(screen, (128,128,128), pygame.Rect(segment[0], segment[1], 10, 10)) # color grey

    def change_direction(self, new_direction):
        self.direction = new_direction
