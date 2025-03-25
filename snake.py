import pygame

class Snake:

    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]  # Initial snake position
        self.direction = (10,0) # kickstart to right
        self.position = self.body[0]
        self.size = 12 # size of each segment
        self.color = (128, 128,128) # grey like 3310
        self.gap = 1 # 1px between each segment

    def move(self, food, game):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        new_head = (new_head[0] % 800, new_head[1] % 600) # go through the wall
        self.body = [new_head] + self.body[:-1] # move snake
        self.position = new_head

        # Affiche les positions pour déboguer
        print(f"Serpent position: {self.position}")
        print(f"Nourriture position: {food.position}")

        # eat food condition
        if self.position == food.position:
            print("Le serpent a mangé la nourriture!")
            self.grow()  # grow the snake with segment+1
            food.spawn()  # Respawn food
            print(f"Respawn food: {food.position}")
            game.score += 1

    def grow(self):
        # add pixel from tail
        tail = self.body[-1]
        self.body.append(tail)
        print(f"Serpent grow, new size: {len(self.body)}")

    def change_direction(self, new_direction):
    # Forbid u-turn : check that the direction is not opposite
        u_turn = (-self.direction[0], -self.direction[1])
        if new_direction != u_turn:
            self.direction = new_direction

    def draw(self, screen):
         for segment in self.body:

            pygame.draw.rect(screen, self.color, pygame.Rect(segment[0] + self.gap, segment[1] + self.gap, self.size - self.gap, self.size - self.gap))

            #if i == 0:  # Dessiner la tête du serpent avec un cercle
            #    pygame.draw.circle(screen, color, (segment[0] + self.size // 2, segment[1] + self.size // 2), 10)
            #else:  # Dessiner les segments du corps avec des rectangles
            #    pygame.draw.rect(screen, self.color, pygame.Rect(segment[0] + self.gap, segment[1] + self.gap, self.size - self.gap, self.size - self.gap))
