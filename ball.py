import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        image = pygame.image.load('assets/ballon.png')
        largeur = 65
        hauteur = 65
        self.image_redimensionnee = pygame.transform.scale(image, (largeur, hauteur))
        self.rect = self.image_redimensionnee.get_rect()
        self.rect.x = 320
        self.rect.y = 390
