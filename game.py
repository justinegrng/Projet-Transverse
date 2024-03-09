import pygame
from goal import Goal
from ball import Ball

class Game:

    def __init__(self):
        self.goal = Goal()
        self.ball = Ball()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.ball.toggle_movement()
                    print("Ballon lancé")

    def update(self):
        self.ball.move()
