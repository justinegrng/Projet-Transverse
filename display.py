import pygame

class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode((700, 460))
        self.background = pygame.image.load('assets/background.png')

    def display_background(self):
        self.screen.blit(self.background, (0, 0))

    def display_goal(self, goal):
        self.screen.blit(goal.image, goal.rect)

    def display_ball(self, ball):
        screenRect = (ball.rect.x, 460 - ball.rect.y)
        self.screen.blit(ball.image_redimensionnee, screenRect)

    def display_quit_button(self, button):
        button.draw(self.screen)

    def update_display(self):
        pygame.display.flip()