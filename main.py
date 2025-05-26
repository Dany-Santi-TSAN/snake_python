import pygame
import asyncio
import sys
import platform
from pathlib import Path
from game_logic.snake import Snake
from game_logic.food import Food
from game_logic.display import Display

# Pygbag compatibility check
PYGBAG = platform.system() == "Emscripten"

class Game:
    # contains all variables and functions necessary for the smooth gameplay
    def __init__(self):
        pygame.init()

        # Initialize mixer with specific settings for web compatibility
        try:
            if PYGBAG:
                # Web-optimized mixer settings
                pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=1024)
            pygame.mixer.init()
        except pygame.error as e:
            print(f"Audio initialization failed: {e}")
            # Continue without audio rather than crash

        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.display = Display()
        self.running = True

        # Sound loading with error handling
        self.sounds_enabled = True
        self.sound_bite = None
        self.sound_speed = None
        self.sound_crash = None

        self.load_sounds()

        self.last_speed_increase_score = 0
        self.reset_game()
        print("Game initialized")

    def load_sounds(self):
        """Load sounds with fallback handling"""
        sound_files = {
            'bite': 'sounds/apple_bite-pygbag.ogg',
            'speed': 'sounds/f1_sound-pygbag.ogg',
            'crash': 'sounds/crash-pygbag.ogg'
        }

        try:
            # Check if files exist
            for name, path in sound_files.items():
                if not Path(path).exists():
                    print(f"Warning: Sound file {path} not found")
                    self.sounds_enabled = False
                    return

            # Load sounds
            self.sound_bite = pygame.mixer.Sound(sound_files['bite'])
            self.sound_speed = pygame.mixer.Sound(sound_files['speed'])
            self.sound_crash = pygame.mixer.Sound(sound_files['crash'])

            # Set volume levels
            if self.sound_bite:
                self.sound_bite.set_volume(0.7)
            if self.sound_speed:
                self.sound_speed.set_volume(0.5)
            if self.sound_crash:
                self.sound_crash.set_volume(0.8)

            print("Sounds loaded successfully")

        except pygame.error as e:
            print(f"Failed to load sounds: {e}")
            self.sounds_enabled = False
        except Exception as e:
            print(f"Unexpected error loading sounds: {e}")
            self.sounds_enabled = False

    def play_sound(self, sound):
        """Safe sound playing with error handling"""
        if self.sounds_enabled and sound:
            try:
                sound.play()
            except pygame.error:
                # Disable sounds if playback fails
                self.sounds_enabled = False

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
            self.play_sound(self.sound_speed)
            print(f"Speed increased to: {self.base_speed} fps")

    async def update(self):
        if not self.game_over:
            self.snake.move()

            # Check for collision with itself
            if self.snake.body[0] in self.snake.body[1:]:
                print("Auto-collision! Game over.")
                self.game_over = True
                self.play_sound(self.sound_crash)
                return

            # Check if snake eat food
            if tuple(map(int, self.snake.body[0])) == tuple(map(int, self.food.position)):
                print(f"Snake head: {self.snake.body[0]} | Food: {self.food.position}")
                print("Snake ate the food!")
                self.snake.grow()
                self.food.spawn()
                self.score += 1
                self.play_sound(self.sound_bite)
                print(f"New score: {self.score}")

            self.update_speed_level()

            # Check for collision with walls
            # (uncomment one of the following options according to your choice)

            # Option 1: Game over if snake hits the wall
            if not (0 <= self.snake.body[0][0] < 600 and 0 <= self.snake.body[0][1] < 600):
                print("Collision with wall! Game over.")
                self.game_over = True
                self.play_sound(self.sound_crash)

            # Option 2: Snake wraps around the screen
            # self.snake.body[0] = (self.snake.body[0][0] % 600, self.snake.body[0][1] % 600)
            # print("Snake wrapped around the screen")

    def draw(self):
        # update the screen with game components
        self.screen.fill((163, 198, 65)) # fill screen with green like 3310 version
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
            self.clock.tick(self.base_speed) # Control the game speed
            await asyncio.sleep(0) # Yield control to the event loop
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
