import pygame
class Goal(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.speed = 2.25
        self.image = pygame.image.load('assets/gardien.png')
        self.rect = self.image.get_rect()
        self.rect.x = 275
        self.rect.y = 200
        self.direction = 1
        self.is_moving = True

    def move_goal(self):
        if self.is_moving:
            self.rect.x += self.speed * self.direction
            if self.rect.x >= 455:
                self.direction = -1
            elif self.rect.x <= 75:
                self.direction = 1
        else:
            self.speed=0