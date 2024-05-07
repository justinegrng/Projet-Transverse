import pygame
from goal import Goal
from ball import Ball
from button import Button
from trajectory import Trajectory


class Game:

    def __init__(self):
        self.goal = Goal()
        self.ball = Ball()
        self.trajectory = Trajectory()
        self.quit_button = Button((194, 255, 255), 550, 400, 100, 50, 'Quit')
        # couleur du bouton, position x, position y, largeur, hauteur, texte, si vous voulez changer.
        self.goal_colors = [(21, 131, 223), (6, 41, 69), (241, 188, 160), (222, 251, 255)]
        # J'ai mis couleurs du gardien dans liste que le contour blanc, short bleu, peau beige et maillot bleu foncé
        self.minimum_force = 10

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.clicked(pygame.mouse.get_pos()):
                    running = False
                    pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.trajectory.game_steering_angle += 1
                elif event.key == pygame.K_RIGHT:
                    self.trajectory.game_steering_angle -= 1
                """if event.key == pygame.K_SPACE:
                    self.ball.ball_trajectory(self.trajectory.game_steering_angle, self.trajectory.strike_force)
"""
    def run_game(self):
        pygame.display.set_caption("Tirs aux buts !")
        screen = pygame.display.set_mode((700, 460))
        background = pygame.image.load('assets/background.png')
        game = Game()
        running = True
        while running:
            if pygame.display.get_init():
                # vérifie si la fenêtre est ouverte car autrement il y a une erreur, même si elle impacte pas c'est mieux
                screen.blit(background, (0, 0))
                screen.blit(game.goal.image, game.goal.rect)
                screen.blit(game.ball.image_redimensionnee, game.ball.rect)
                self.quit_button.draw(screen)
                pygame.display.flip()
                self.handle_events()
                game.goal.move_goal()
                game.trajectory.update_trajectory_angle()
                game.trajectory.update_strike_force()
                game.ball.update_ball()
        pygame.quit()
