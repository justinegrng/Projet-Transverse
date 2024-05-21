import pygame


class Trajectory(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.start_steering_angle = 0
        self.game_steering_angle = self.start_steering_angle
        self.start_strike_force = 77
        self.strike_force = self.start_strike_force
        self.minimal_force = self.start_strike_force
        self.maximal_force = 82
        self.maximal_angle = 50


    def trajectory_left_right(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.game_steering_angle -= 0.3
        if keys[pygame.K_LEFT]:
            self.game_steering_angle += 0.3


    def strike_force_calculation(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:

            self.strike_force += 0.01
        else:
            self.strike_force -= 0.01

    def update_strike_force(self):
        self.strike_force_calculation()
        if self.strike_force > self.maximal_force:
            self.strike_force = self.maximal_force
        elif self.strike_force < self.minimal_force:
            self.strike_force = self.minimal_force

    def update_trajectory_angle(self):
        self.trajectory_left_right()
        if self.game_steering_angle > self.maximal_angle:
            self.game_steering_angle = self.maximal_angle
        elif self.game_steering_angle < -self.maximal_angle:
            self.game_steering_angle = -self.maximal_angle
        print(self.game_steering_angle)

    def reseting_trajectoire(self):
        self.game_steering_angle = self.start_steering_angle
        self.strike_force = self.start_strike_force
        self.space_pressed = False
        print("parameter reset")

