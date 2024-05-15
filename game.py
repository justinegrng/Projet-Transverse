from time import sleep

import pygame
from goal import Goal
from ball import Ball
from button import Button
from trajectory import Trajectory
from display import Display


class Game:

    def __init__(self):
        self.goal = Goal()
        self.ball = Ball()
        self.trajectory = Trajectory()
        self.quit_button = Button((194, 255, 255), 550, 400, 100, 50, 'Quit')
        # couleur du bouton, position x, position y, largeur, hauteur, texte, si vous voulez changer.

        # self.goal_colors = [(21, 131, 223), (6, 41, 69), (241, 188, 160), (222, 251, 255)]

        # J'ai mis couleurs du gardien dans liste que le contour blanc, short bleu, peau beige et maillot bleu foncé
        self.minimum_force = 10
        self.display = Display()
        self.force = 0
        self.angle = 0

    def handle_events(self):

        ball_position = []

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
                    self.trajectory.game_steering_angle -= 1
                elif event.key == pygame.K_RIGHT:
                    self.trajectory.game_steering_angle += 1
                if event.key == pygame.K_SPACE:

                    self.angle = 0
                    self.force = 70 # pb <80


    def run_game(self):
        pygame.display.set_caption("Tirs aux buts !")
        screen = pygame.display.set_mode((700, 460))
        running = True
        while running:
            if pygame.display.get_init():
                self.display.display_background()
                # vérifie si la fenêtre est ouverte car autrement il y a une erreur, même si elle impacte pas c'est mieux
                self.display.display_goal(self.goal)
                self.display.display_ball(self.ball)
                self.display.display_quit_button(self.quit_button)
                self.display.update_display()
                self.quit_button.draw(screen)
                # mise à jour des événements du jeu
                self.handle_events()

                self.trajectory.update_trajectory_angle()
                self.trajectory.update_strike_force()
                if self.force != 0 and self.ball.moving and not self.ball.colision:
                    print('espace')
                    if self.ball.width > 30 or self.ball.rect.y > 150:
                        self.ball.moveBall(self.angle, self.force)
                        self.display.display_ball(self.ball)
                        self.ball.resize_image()
                        self.ball.update_ball()
                        print('mise à jour')
                    else:
                        self.ball.moving = False
                        print('ball.moving')
                        sleep(0.5)
                else:
                    self.ball.reseting_settings()
                    self.goal.move_goal()
                    self.force = 0
                    self.angle = 0
                sleep(0.0001)


        pygame.quit()
