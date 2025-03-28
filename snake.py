import pygame

class Snake:
    # Contains the specific Snake logic
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]  # Initial snake position with 3 segments
        self.direction = (10, 0)  # Initial direction (right)
        self.size = 10  # Size of each segment (pixel)
        self.color = (128, 128, 128)  # Grey color
        print(f"Snake initialized at: {self.body[0]}")

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        print(f"Moving snake from {head} to {new_head}")
        self.body = [new_head] + self.body[:-1]  # Move snake

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)  # Grow the snake
        print(f"Snake grew, new size: {len(self.body)}")

    def change_direction(self, new_direction):
        # Forbid u-turn: check that the direction is not opposite
        u_turn = (-self.direction[0], -self.direction[1])
        if new_direction != u_turn:
            self.direction = new_direction
            print(f'Direction changed to: {self.direction}')
        else:
            print('U-turn is forbidden')

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, pygame.Rect(segment[0], segment[1], self.size, self.size))
