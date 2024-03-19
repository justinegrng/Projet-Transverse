import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        image = pygame.image.load('assets/ballon.png')
        largeur = 65
        hauteur = 65
        self.image_redimensionnee = pygame.transform.scale(image, (largeur, hauteur))
        self.rect = self.image_redimensionnee.get_rect()
        self.start_x = 320
        self.start_y = 390
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.moving = False
        self.speed = 5

    def toggle_movement(self):
        self.moving = not self.moving

    def move(self):
        if self.moving:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.x = self.start_x
                self.rect.y = self.start_y
                self.moving = False
