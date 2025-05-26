import pygame
import random


class Food:
    def __init__(self):
        # self.spawn()
        # self.image = pygame.image.load("sprite/apple_sprite.png")
        # self.image = pygame.transform.scale(self.image, (10, 10))
        self.size = 10  # Taille carrée de la pomme
        self.position = (100, 100)
        self.spawn()
        print("Food initialized")

    def spawn(self, snake_body=None):
        while True:
            new_position = (random.randint(0, 59) * self.size, random.randint(0, 59) * self.size)
            if snake_body is None or new_position not in snake_body:
                break

        self.position = new_position
        print(f"New food spawned at: {self.position}")

    # def spawn(self):
    # Random spawn within the 600x600 screen limit
    # self.position = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
    # print(f"Food spawned at: {self.position}")

    # def draw(self, screen):
    # screen.blit(self.image, self.position)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position[0], self.position[1], 10, 10))
