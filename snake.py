import pygame
from game import Game
from food import Food

class Snake:

    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]  # Initial snake position
        self.direction = (10,0) # kickstart to right
        self.position = self.body[0]

    def move(self, food, game):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        new_head = (new_head[0] % 800, new_head[1] % 600) # go through the wall
        self.body = [new_head] + self.body[:-1] # move snake
        self.position = new_head

        # Vérifier la collision avec la nourriture
        if self.position == food.position:
            self.grow()  # Faire grandir le serpent
            food.spawn()  # Respawn de la nourriture
            game.score += 10  # Ajouter 10 points au score

    def grow(self):
        # add pixel from tail
        tail = self.body[-1]
        self.body.append(tail)

    def change_direction(self, new_direction):
    # Forbid u-turn : check that the direction is not opposite
        opposite_direction = (-self.direction[0], -self.direction[1])
        if new_direction != opposite_direction:
            self.direction = new_direction

    def draw(self, screen):
        for segment in self.body:
            # draw each segment
            pygame.draw.rect(screen, (128,128,128), pygame.Rect(segment[0], segment[1], 10, 10)) # color grey
