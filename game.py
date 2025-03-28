import pygame
from snake import Snake
from food import Food
from display import Display

class Game :
    # contains all variables and functions necessary for the smooth gameplay

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600)) # screen size
        pygame.display.set_caption('Snake Game') # title
        self.clock = pygame.time.Clock() #speed (fps)
        self.display = Display()
        self.running = True
        self.reset_game()
        print("Game initialized")

    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.base_speed = 5
        self.game_over = False


    def handle_events(self):
        # basic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # restart
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        self.game_over = False
                        print("Game restarted")

        # keyboard
                else:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -10))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, 10))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-10, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((10, 0))

    def update(self):
        if not self.game_over:
            self.snake.move()

            # Check for collision with itself
            if self.snake.body[0] in self.snake.body[1:]:
                print("Auto-collision! Game over.")
                self.game_over = True
                return

            # check if snake eat food
            if self.snake.body[0] == self.food.position:
                print("Snake ate the food!")
                self.snake.grow()
                self.food.spawn()
                self.score += 1
                print(f"New score: {self.score}")

            # Check for collision with walls
            # (uncomment one of the following options according your choice)

            # Option 1: Game over if snake hits the wall
            if not (0 <= self.snake.body[0][0] < 600 and 0 <= self.snake.body[0][1] < 600):
                print("Collision with wall! Game over.")
                self.game_over = True

            # Option 2: Snake wraps around the screen
            # self.snake.body[0] = (self.snake.body[0][0] % 600, self.snake.body[0][1] % 600)

    def draw(self):
        # update the screen with game components
        self.screen.fill((163,198,65)) #fill screen with green like 3310 version
        if self.game_over:
            self.display.display_game_over(self.screen)
        else:
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.display.display_score(self.screen, self.score)  # Display score
            self.display.display_speed(self.screen, self.clock) # Display speed
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.base_speed)  # Control the game speed

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
