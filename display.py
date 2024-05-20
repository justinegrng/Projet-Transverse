import pygame
from trajectory import Trajectory


class Display:
    def __init__(self, ball, goal):
        self.trajectory = Trajectory()
        self.goal = goal
        self.ball = ball
        self.screen = pygame.display.set_mode((700, 460))
        self.background = pygame.image.load('assets/background.png')

    def display_background(self):
        self.screen.blit(self.background, (0, 0))

    def display_goal(self):
        self.screen.blit(self.goal.image, self.goal.rect)

    def display_ball(self):
        screen_rect = (self.ball.rect.x, 460 - self.ball.rect.y)
        self.screen.blit(self.ball.image_redimensionnee_rotate, screen_rect)

    def display_quit_button(self, button):
        button.draw(self.screen)

    def update_display(self):
        pygame.display.flip()

    def display_ball_and_goal(self):
        if self.trajectory.strike_force > 95:
            if self.ball.width < 50 or self.ball.rect.y < 120 or self.ball.rect.y > 400 or self.ball.collision:
                self.display_ball()
                self.display_goal()
        else:
            self.display_goal()
            self.display_ball()
