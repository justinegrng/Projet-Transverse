import pygame
import time


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

    # variable globale pour stocker le temps durant lequel le bouton à été pressé
    button_pressed_time = None

    def handle_button_press(self):
        """
        enregistre le temps durant lequel le bouton à été pressé
        """
        global button_pressed_time
        button_pressed_time = time.time()
        return button_pressed_time

    def handle_button_release(self):
        pass


def get_shooting_speed(pressed_time):
    """
    Calcule la vitesse selon le temps que le bouton à été pressé
    """
    # Calcule le temps écoulé depuis que le bouton était pressé
    time_elapsed = time.time() - pressed_time

    # Défini un temps maximum (à ajuster si besoin)
    max_time_threshold = 2.0

    # Calcule la vitesse selon le temps
    shooting_speed = min(1.0, time_elapsed / max_time_threshold) * 10.0

    return shooting_speed
