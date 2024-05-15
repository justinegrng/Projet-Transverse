import pygame

class Trajectory(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # Création angle de direction + variable temps 1(force augmente)/variable temps2(force baisse)--> à modéliser par carrée dont la longueur augmente
        self.start_steering_angle = 0
        self.game_steering_angle = self.start_steering_angle
        self.time_up_released = 0
        self.game_time_up_released = self.time_up_released
        self.time_up_pressed = 0
        self.game_time_up_pressed = self.time_up_pressed
        self.strike_force = 0
        self.minimal_force = 10
        self.maximal_force = 100

    def trajectory_left_right(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:

            self.game_steering_angle += 0.2
        if keys[pygame.K_LEFT]:
            self.game_steering_angle -= 0.2


    def strike_force_calculation(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.game_time_up_pressed += 0.2
        else:
            self.game_time_up_released += 0.2


    def update_strike_force(self):
        self.strike_force_calculation()
        if self.game_time_up_pressed - self.game_time_up_released >= self.minimal_force and self.game_time_up_pressed - self.game_time_up_released <= self.maximal_force:
            self.strike_force = self.game_time_up_pressed - self.game_time_up_released
        elif self.game_time_up_pressed - self.game_time_up_released < self.minimal_force:
            self.strike_force = self.minimal_force
        elif self.game_time_up_pressed - self.game_time_up_released > self.maximal_force:
            self.strike_force = self.maximal_force
    #print(self.strike_force)

    def update_trajectory_angle(self):
        """self.trajectory_left_right()
        if self.game_steering_angle > 90:
            self.game_steering_angle = 90
        elif self.game_steering_angle < -90:
            self.game_steering_angle = -90"""
        self.game_steering_angle=45

