import pygame


class Goal(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.speed = 2.25
        self.image = pygame.image.load('assets/gardien1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 275
        self.rect.y = 185
        self.direction = 1
        self.is_moving = True
        self.goal_colors = [(0, 255, 0), (254, 219, 66), (211, 32, 26), (245, 183, 128),
                            (191, 119, 26)]

    def move_goal(self):
        if self.is_moving:
            self.rect.x += self.speed * self.direction
            if self.rect.x >= 445:
                self.direction = -1
            elif self.rect.x <= 100:
                self.direction = 1
        else:
            self.speed = 0

