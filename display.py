import pygame

class Display:
    def display_game_over(self, screen):
        font = pygame.font.Font(None, 74)
        game_over_text = font.render('Game Over', True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(game_over_text, text_rect)
        pygame.display.flip()

        # Wait for key press
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    waiting_for_input = False

    def display_score(self, screen, score, player_name):
        font = pygame.font.SysFont('Arial', 24)
        score_text = font.render(f"{player_name} | Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def display_speed(self, screen, clock):
        font = pygame.font.SysFont('Arial', 24)
        speed_text = font.render(f"Speed: {clock.get_fps():.1f}", True, (255, 255, 255))
        screen.blit(speed_text, (10, 40))

    def home_screen(self, screen, font, player_name, best_score):
        screen.fill((0, 0, 0))

        title = font.render("Snake Game", True, (255, 255, 255))
        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 80))

        input_text = font.render(f"Enter your name: {player_name}", True, (255, 255, 255))
        screen.blit(input_text, (screen.get_width()//2 - input_text.get_width()//2, 180))

        best_score_text = font.render(f"Best Score: {best_score}", True, (255, 255, 255))
        screen.blit(best_score_text, (screen.get_width()//2 - best_score_text.get_width()//2, 250))

        start_text = font.render("Press ENTER to Start", True, (0, 255, 0))
        screen.blit(start_text, (screen.get_width()//2 - start_text.get_width()//2, 350))

        pygame.display.flip()

    def leaderboard(self, screen, font, leaderboard):
        screen.fill((0, 0, 0))

        title = font.render("Leaderboard", True, (255, 255, 0))
        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 50))

        for idx, (name, score) in enumerate(leaderboard[:5]):  # Top 5
            line = font.render(f"{idx+1}. {name}: {score}", True, (255, 255, 255))
            screen.blit(line, (screen.get_width()//2 - line.get_width()//2, 150 + idx * 40))

        pygame.display.flip()
