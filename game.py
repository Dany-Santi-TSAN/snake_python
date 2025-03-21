import pygame
from snake import Snake
from food import Food

class Game :
    # contains all variables and functions necessary for the smooth gameplay

    def __init__(self):
        # initialize windows, title and clock
        self.screen = pygame.display.set_mode((800, 600)) # windows
        pygame.display.set_caption('Snake Game') # title
        self.clock = pygame.time.Clock() # clock
        self.running = True
        self.snake = Snake()
        self.food = Food()

    def handle_events(self):
        # handle event such as quitting
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def update(self):
        # update the screen with game components
        self.screen.fill((163,198,65)) #fill screen with green like 3310 version
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()
        pygame.display.flip() #refresh

    def run(self):
        # main game loop
        while self.running: # Keep the game running until quitting
         self.handle_events()
         self.update()
         self.clock.tick(60) # Limit for 60 FPS
