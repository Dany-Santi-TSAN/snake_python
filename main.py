import pygame

class Game :
    # contains all variables and functions necessary for the smooth gameplay

    def __init__(self):
        # initialize windows, title and clock
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        # handle event such as quitting
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def update(self):
        # update the screen with game components
        self.screen.fill((0,0,0)) #fill screen with dark color
        pygame.display.flip() #refresh

    def run(self):
        # main game loop
        while self.running: # Keep the game running until quitting
         self.handle_events()
         self.update()
         self.clock.tick(60) # Limit for 60 FPS

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
