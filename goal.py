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
        self.rect.x += self.speed * self.direction
        if self.rect.x >= 500:
            self.direction = -1
        elif self.rect.x <= 0:
            self.direction = 1


    def toggle_movement(self):
        self.is_moving = False
