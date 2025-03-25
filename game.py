import pygame
import sys
from snake import Snake
from food import Food
from display import Display

class Game :
    # contains all variables and functions necessary for the smooth gameplay

    def __init__(self):
        # initialize windows, title and clock
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600)) # windows
        pygame.display.set_caption('Snake Game') # title
        self.clock = pygame.time.Clock() # speed
        self.font = pygame.font.SysFont('Arial', 36) # front

        self.running = True
        self.state = "HOME"  # "HOME", "PLAY", "GAME_OVER"

        self.player_name = ""
        self.best_score = 0
        self.input_active = True
        self.playing = False

        self.snake = Snake()
        self.food = Food()
        self.display = Display()
        self.score = 0
        self.base_speed = 5

        self.leaderboard = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif self.state == "HOME" and event.type == pygame.KEYDOWN:
                if self.input_active:
                    if event.key == pygame.K_RETURN:
                        self.state = "PLAY"
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    else:
                        if len(self.player_name) < 10 and event.unicode.isprintable():
                            self.player_name += event.unicode

            elif self.state == "PLAY" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction((0, -10))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, 10))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction((-10, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((10, 0))

    def update(self):
        # update the screen with game components
        self.screen.fill((163,198,65)) #fill screen with green like 3310 version
        self.snake.move(self.food, self)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.display.display_score(self.screen, self.score, self.player_name)
        self.display.display_speed(self.screen, self.clock)
        pygame.display.flip() #refresh

    def collision(self):
        # game over if collision with body
        if self.snake.body[0] in self.snake.body[1:]:
            self.state = "GAME_OVER"
            self.display.display_game_over(self.screen)
            self.update_leaderboard()
            self.reset_game()

    def eat_food(self):
        # check if snake eat food
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.spawn() # respawn food
            self.score += 1

    def reset_game(self):
    # Réinitialiser les éléments du jeu
        self.snake = Snake()  # Réinitialiser le serpent
        self.food = Food()  # Réinitialiser la nourriture
        self.best_score = max(self.best_score, self.score) # keep best score
        self.score = 0

    def update_leaderboard(self):
        self.leaderboard.append((self.player_name, self.score))
        self.leaderboard.sort(key=lambda x: x[1], reverse=True)
        self.leaderboard = self.leaderboard[:5]

    def run(self):
        # main game loop
        while self.running: # Keep the game running until quitting
            self.handle_events()

            if self.state == "HOME":
                self.display.home_screen(self.screen, self.font, self.player_name, self.best_score)

            elif self.state == "PLAY":
                self.snake.move(self.food, self)
                self.eat_food()
                self.update()
                self.collision()
                speed = min(self.base_speed + ((self.score // 10)*5), 30) # Limit to 30 fps
                self.clock.tick(speed)

            elif self.state == "GAME_OVER":
                self.display.leaderboard(self.screen, self.font, self.leaderboard)
                pygame.time.wait(3000)
                self.state = "HOME"
