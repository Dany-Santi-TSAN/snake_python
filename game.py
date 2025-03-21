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
        self.score = 0

    def handle_events(self):
        # handle event such as quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        # add keypad
            elif event.type == pygame.KEYDOWN:
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
        self.display_score()
        pygame.display.flip() #refresh

    def display_score(self):
        # Afficher le score en haut à gauche de l'écran
        font = pygame.font.SysFont('Arial', 24)  # Police de caractère
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))  # Texte du score
        self.screen.blit(score_text, (10, 10))  # Afficher le score à l'écran

    def collision(self):
        # game over if collision with body
        if self.snake.body[0] in self.snake.body[1:]:
            self.running = False
            self.display_game_over()
            self.reset_game()

    def eat_food(self):
        # check if snake eat food
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.spawn() # respawn food
            self.score += 10

    def reset_game(self):
    # Réinitialiser les éléments du jeu
        self.snake = Snake()  # Réinitialiser le serpent
        self.food = Food()  # Réinitialiser la nourriture
        self.running = True  # Recommencer le jeu
        self.score = 0

    def display_game_over(self):
    # Display "Game Over" in middle of screen
        font = pygame.font.Font(None, 74)  # Font size
        game_over_text = font.render('Game Over', True, (255, 0, 0))  # Game Over in red
        text_rect = game_over_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))  # middle screen
        self.screen.blit(game_over_text, text_rect)  # display text on screen
        pygame.display.flip()  # Refresh

            # Attendre que le joueur appuie sur une touche pour redémarrer
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:  # Attente d'une touche pour redémarrer
                    waiting_for_input = False


    def run(self):
        # main game loop
        while self.running: # Keep the game running until quitting
         self.handle_events()
         self.eat_food()
         self.update()
         self.collision()
         self.clock.tick(10) # Limit for 60 FPS
