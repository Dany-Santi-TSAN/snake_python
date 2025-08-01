import pygame
import asyncio
import platform
from pathlib import Path
from game_logic.snake import Snake
from game_logic.food import Food
from game_logic.display import Display
from audio_manager import AudioManager

# Pygbag compatibility check
PYGBAG = platform.system() == "Emscripten"


class Game:
    # contains all variables and functions necessary for the smooth gameplay
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.display = Display()
        self.running = True

        # Initialize audio manager
        self.audio = AudioManager()
        self.load_sounds()

        self.last_speed_increase_score = 0
        self.reset_game()
        print("Game initialized")

    def load_sounds(self):
        """Load all game sounds"""
        self.audio.load_sound("bite", "sounds/apple_bite-pygbag.ogg")
        self.audio.load_sound("speed", "sounds/f1_sound-pygbag.ogg")
        self.audio.load_sound("crash", "sounds/crash-pygbag.ogg")

        # Set specific volumes
        self.audio.set_volume("bite", 0.7)
        self.audio.set_volume("speed", 0.5)
        self.audio.set_volume("crash", 0.8)

        print("Sounds loaded successfully")

    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.base_speed = 6
        self.game_over = False

    async def handle_events(self):
        # basic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # restart
            elif event.type == pygame.KEYDOWN:
                # Unlock audio on first key press (required for web browsers)
                if not self.audio.audio_unlocked:
                    self.audio.unlock_audio()

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

    def update_speed_level(self):
        # rise speed every 5 points
        if self.score > 0 and self.score % 5 == 0 and self.score != self.last_speed_increase_score:
            self.base_speed = min(30, self.base_speed + 2)
            self.last_speed_increase_score = self.score
            self.audio.play_sound("speed")
            print(f"Speed increased to: {self.base_speed} fps")

    async def update(self):
        if not self.game_over:
            self.snake.move()

            # Check for collision with itself
            if self.snake.body[0] in self.snake.body[1:]:
                print("Auto-collision! Game over.")
                self.game_over = True
                self.audio.play_sound("crash")
                return

            # Check if snake eat food
            if tuple(map(int, self.snake.body[0])) == tuple(map(int, self.food.position)):
                print(f"Snake head: {self.snake.body[0]} | Food: {self.food.position}")
                print("Snake ate the food!")
                self.snake.grow()
                self.food.spawn()
                self.score += 1
                self.audio.play_sound("bite")
                print(f"New score: {self.score}")

            self.update_speed_level()

            # Check for collision with walls
            # (uncomment one of the following options according to your choice)

            # Option 1: Game over if snake hits the wall
            if not (0 <= self.snake.body[0][0] < 600 and 0 <= self.snake.body[0][1] < 600):
                print("Collision with wall! Game over.")
                self.game_over = True
                self.audio.play_sound("crash")

            # Option 2: Snake wraps around the screen
            # self.snake.body[0] = (self.snake.body[0][0] % 600, self.snake.body[0][1] % 600)
            # print("Snake wrapped around the screen")

    def draw(self):
        # update the screen with game components
        self.screen.fill((163, 198, 65))  # fill screen with green like 3310 version
        if self.game_over:
            self.display.display_game_over(self.screen)
        else:
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.display.display_score(self.screen, self.score)
            self.display.display_speed(self.screen, self.clock)
        pygame.display.flip()

    async def run(self):
        print("Game started")
        while self.running:
            await self.handle_events()
            await self.update()
            self.draw()
            self.clock.tick(self.base_speed)  # Control the game speed
            await asyncio.sleep(0)  # Yield control to the event loop
        pygame.quit()


async def main():
    game = Game()
    await game.run()


if __name__ == "__main__":
    if PYGBAG:
        import pygbag.aio

        pygbag.aio.run(main())
    else:
        asyncio.run(main())
