import pygame
from goal import Goal
import math
from time import sleep

from trajectory import Trajectory


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.goal = Goal()
        self.image = pygame.image.load('assets/ballon.png')
        self.original_image = self.image.copy()
        self.start_width = 70
        self.start_height = 70
        self.width = self.start_width
        self.height = self.start_height
        self.image_redimensionnee = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image_redimensionnee.get_rect()
        self.start_x = 320
        self.start_y = 75
        
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.moving = True
        self.speed_x = 0
        self.speed_y = 0
        self.delta_t = 0.1
        self.shrinkage_coefficient = 0.994
        self.iteration = False
        self.colision = False
        self.goal_colors = [(21, 131, 223), (6, 41, 69), (241, 188, 160), (222, 251, 255)]

    def update_ball(self):
        if self.width <= 40 and self.width >= 30:
            if self.rect.colliderect(self.goal.rect):
                for x in range(self.rect.width):
                    for y in range(self.rect.height):
                        ball_x = self.rect.x + x - self.goal.rect.x
                        ball_y = self.rect.y + y - self.goal.rect.y
                        if (
                                0 <= ball_x < self.goal.image.get_width() and 0 <= ball_y < self.goal.image.get_height() and self.goal.image.get_at(
                            (ball_x, ball_y)) in self.goal_colors):
                            self.colision = True
                            print("Le gardien a arrêté le ballon !")
                            self.moving = False
                            return

    def resize_image(self):
        self.width = self.width * self.shrinkage_coefficient
        self.height = self.height * self.shrinkage_coefficient
        self.image_redimensionnee = pygame.transform.scale(self.original_image, (self.width, self.height))
        self.rect = self.image_redimensionnee.get_rect(center=self.rect.center)

    def moveBall(self, angle, force):
        if not self.iteration:
            self.speed_x = force
            self.speed_y = force
            self.iteration = True
        else:
            self.rect.x = self.rect.x + (self.speed_x * math.cos(math.radians(force)) * self.delta_t) * math.cos(
                math.radians(90 + angle))
            self.rect.y = self.rect.y + self.delta_t * (self.speed_y - (9.81 * self.delta_t))
            self.speed_y -= 9.81 * self.delta_t

    def reseting_settings(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.width = self.start_width
        self.height = self.start_height
        self.resize_image()
        self.speed_x = 0
        self.speed_y = 0
        self.iteration = False
        self.colision = False
        self.moving = True
