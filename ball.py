import pygame
from goal import Goal
import math
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
        self.start_y = 385
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.moving = False


    def update_ball(self):
        if self.rect.colliderect(self.goal.rect):
            for x in range(self.rect.width):
                for y in range(self.rect.height):
                    ball_x = self.rect.x + x - self.goal.rect.x
                    ball_y = self.rect.y + y - self.goal.rect.y
                    if (
                            0 <= ball_x < self.goal.image.get_width() and 0 <= ball_y < self.goal.image.get_height() and self.goal.image.get_at(
                        (ball_x, ball_y)) in self.goal_colors):
                        print("Le gardien a arrêté le ballon !")
                        self.rect.x = self.start_x
                        self.rect.y = self.start_y
                        self.moving = False
                        return
