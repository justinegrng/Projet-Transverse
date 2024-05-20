from time import sleep

import pygame
from goal import Goal
from ball import Ball
from button import Button
from gauge import Gauge
from trajectory import Trajectory
from display import Display


class Game:

    def __init__(self):
        self.goal = Goal()
        self.ball = Ball()
        self.trajectory = Trajectory()
        self.pressed = {}
        self.quit_button = Button((194, 255, 255), 550, 400, 100, 50, 'Quit')
        self.gauge = Gauge((0, 255, 0), 440, 50, 10, 50, self.trajectory.strike_force)
        self.display = Display(self.ball, self.goal)
        self.force = 0
        self.angle = 0
        self.choice_button = False
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.display.button_play_rect.collidepoint(event.pos):
                    self.choice_button = True
                elif self.quit_button.clicked(pygame.mouse.get_pos()):
                    self.running = False
                    pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.pressed[event.key] = True
                if event.key == pygame.K_LEFT:
                    self.pressed[event.key] = True
                if event.key == pygame.K_UP:
                    self.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    self.angle = self.trajectory.game_steering_angle
                    self.force = self.trajectory.strike_force
                    self.gauge = Gauge((0, 255, 0), 440, 50, 10, 50, self.force)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.pressed[event.key] = False
                if event.key == pygame.K_LEFT:
                    self.pressed[event.key] = False

    def run_game(self):
        pygame.display.set_caption("Tirs aux buts !")
        screen = pygame.display.set_mode((700, 460))
        while self.running:
            if self.choice_button:
                if pygame.display.get_init():
                    self.display.display_background()
                    # vérifie si la fenêtre est ouverte car autrement il y a une erreur, même si elle impacte pas c'est mieux
                    self.display.display_ball_and_goal()
                    self.display.display_quit_button(self.quit_button)
                    self.display.display_gauge(self.gauge)
                    self.display.update_display()
                    self.quit_button.draw(screen)

                    # mise à jour des événements du jeu
                    self.handle_events()

                    if self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_LEFT):
                        self.trajectory.update_trajectory_angle()
                    if self.pressed.get(pygame.K_UP):
                        self.trajectory.update_strike_force()
                    if self.force != 0 and self.ball.moving:
                        if (self.ball.width > 30 or self.ball.rect.y > 150) and not self.ball.collision:
                            self.ball.move_ball(self.angle, self.force)
                            self.display.display_ball()
                            self.ball.resize_image()
                            self.ball.ball_rotation()
                            if self.force < 80:
                                self.ball.check_collision(self.goal)
                                if self.ball.collision:
                                    self.trajectory.reseting_trajectoire()
                        else:
                            if not self.ball.moving :
                                if self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_LEFT):
                                    self.trajectory.update_trajectory_angle()
                                if self.pressed.get(pygame.K_UP):
                                    self.trajectory.update_strike_force()
                                self.gauge.draw(screen)

                            self.ball.moving = False
                            self.trajectory.reseting_trajectoire()
                            sleep(1)
                    else:
                        self.gauge = Gauge((0, 255, 0), 440, 50, 10, 50, self.trajectory.strike_force)
                        self.ball.reseting_settings()
                        self.goal.move_goal()
                        self.force = 0
                        self.angle = 0
                    print(self.ball.score)
                    sleep(0.0001)
            else:
                self.display.display_start_menu()

            self.handle_events()

        pygame.quit()
