import pygame
from goal import Goal
import math


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
        self.image_redimensionnee_rotate = self.image_redimensionnee.copy()
        self.start_x = 328
        self.start_y = 75

        self.rect.x = self.start_x
        self.rect.y = self.start_y

        self.float_x = self.start_x
        self.float_y = self.start_y

        self.moving = False
        self.speed_x = 0
        self.speed_y = 0
        self.delta_t = 0.04
        self.shrinkage_coefficient = 0.997
        self.iteration = False
        self.collision = False
        self.angle_rotation = 0
        self.score = 0

    def resize_image(self):
        self.width = self.width * self.shrinkage_coefficient
        self.height = self.height * self.shrinkage_coefficient
        self.image_redimensionnee = pygame.transform.scale(self.original_image, (self.width, self.height))
        self.rect = self.image_redimensionnee.get_rect(center=self.rect.center)

    def ball_rotation(self):
        self.angle_rotation += 1
        self.image_redimensionnee_rotate = pygame.transform.rotate(self.image_redimensionnee, self.angle_rotation)
        self.rect = self.image_redimensionnee_rotate.get_rect(center=self.rect.center)

    def move_ball(self, angle, force):
        if not self.iteration:
            self.speed_x = force
            self.speed_y = force
            self.iteration = True
        else:
            self.float_x = self.float_x + (self.speed_x * math.cos(math.radians(force)) * self.delta_t) * math.cos(
                math.radians(90 + angle))
            self.float_y = self.float_y + self.delta_t * (self.speed_y - (9.81 * self.delta_t))
            self.speed_y -= 9.81 * self.delta_t

            self.rect.x = self.float_x
            self.rect.y = self.float_y

    def check_collision(self, goal):
        if self.width <= 30:
            # Récupérer pixel des images
            ball_pixels = pygame.mask.from_surface(self.image_redimensionnee_rotate)
            goal_pixels = pygame.mask.from_surface(goal.image)

            # Calcul décalage
            offset = (self.rect.x - goal.rect.x, self.rect.y - goal.rect.y)

            # regarde si collision avec colors image
            for x in range(ball_pixels.get_size()[0]):
                for y in range(ball_pixels.get_size()[1]):
                    if ball_pixels.get_at((x, y)):
                        goal_x = x + offset[0]
                        goal_y = y + offset[1]
                        if 0 <= goal_x < goal_pixels.get_size()[0] and 0 <= goal_y < goal_pixels.get_size()[1]:
                            color = goal.image.get_at((goal_x, goal_y))[:3]
                            if color in self.goal.goal_colors:
                                self.collision = True
                                self.moving = False
                                print("Collision detected at", (goal_x, goal_y))
                                self.score += 1
                                return

    def reseting_settings(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.float_x = self.start_x
        self.float_y = self.start_y
        self.width = self.start_width
        self.height = self.start_height
        self.image_redimensionnee_rotate = pygame.transform.scale(self.original_image, (self.width, self.height))

        self.resize_image()
        self.speed_x = 0
        self.speed_y = 0
        self.iteration = False

        self.collision = False
        self.moving = True
