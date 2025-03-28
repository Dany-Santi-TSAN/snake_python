import pygame

class Display:
    # Contains display logic

    def __init__(self):
        pygame.font.init()  # Initialize font module

    def display_game_over(self, screen):
        font = pygame.font.SysFont(None, 40)

        # Add text
        lines = ["Game Over !", "Press 'R' to Restart"]

        # Pos in middle of screen
        x = screen.get_width() // 2
        y = screen.get_height() // 2.3

        for i, line in enumerate(lines):
            text_surface = font.render(line, True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(x, y + i * 40)) # gap between line
            screen.blit(text_surface, text_rect)

    def display_score(self, screen, score):
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def display_speed(self, screen, clock):
        font = pygame.font.SysFont('Arial', 24)
        speed_text = font.render(f"Speed: {clock.get_fps():.1f}", True, (255, 255, 255))
        screen.blit(speed_text, (10, 40))
