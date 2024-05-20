import pygame
from trajectory import Trajectory


class Display:
    def __init__(self, ball, goal):
        self.trajectory = Trajectory()
        self.goal = goal
        self.ball = ball
        self.screen = pygame.display.set_mode((700, 460))
        self.background = pygame.image.load('assets/background.png')
        self.button_play = pygame.image.load('assets/button_play.png')
        self.button_play_rect = self.button_play.get_rect(center=(350, 230))

    def display_background(self):
        self.screen.blit(self.background, (0, 0))

    def display_goal(self):
        self.screen.blit(self.goal.image, self.goal.rect)

    def display_ball(self):
        screen_rect = (self.ball.rect.x, 460 - self.ball.rect.y)
        self.screen.blit(self.ball.image_redimensionnee_rotate, screen_rect)

    def display_quit_button(self, button):
        button.draw(self.screen)

    def display_gauge(self, gauge):
        gauge.draw(self.screen)

    def display_start_menu(self):
        self.display_background()
        self.screen.blit(self.button_play, self.button_play_rect.topleft)
        pygame.display.flip()

    def update_display(self):
        pygame.display.flip()

    def display_ball_and_goal(self):
        if self.trajectory.strike_force >= 80:
            if self.ball.width < 50 or self.ball.rect.y < 120 or self.ball.rect.y > 400 or self.ball.collision:
                self.display_ball()
                self.display_goal()
        else:
            self.display_goal()
            self.display_ball()

