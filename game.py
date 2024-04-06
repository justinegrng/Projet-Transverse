import pygame
from goal import Goal
from ball import Ball, get_shooting_speed
from button import Button


class Game:

    def __init__(self):
        self.goal = Goal()
        self.ball = Ball()
        self.quit_button = Button((194, 255, 255), 550, 400, 100, 50, 'Quit')
        # couleur du bouton, position x, position y, largeur, hauteur, texte, si vous voulez changer.
        self.goal_colors = [(21, 131, 223), (6, 41, 69), (241, 188, 160), (222, 251, 255)]
        # J'ai mis couleurs du gardien dans liste que le contour blanc, short bleu, peau beige et maillot bleu foncé

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.clicked(pygame.mouse.get_pos()):
                    running = False
                    pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.ball.toggle_movement()

    def update(self):
        self.ball.move()
        if self.ball.rect.colliderect(self.goal.rect):
            for x in range(self.ball.rect.width):
                for y in range(self.ball.rect.height):
                    ball_x = self.ball.rect.x + x - self.goal.rect.x
                    ball_y = self.ball.rect.y + y - self.goal.rect.y
                    if (
                            0 <= ball_x < self.goal.image.get_width() and 0 <= ball_y < self.goal.image.get_height() and self.goal.image.get_at(
                            (ball_x, ball_y)) in self.goal_colors):
                        print("Le gardien a arrêté le ballon !")
                        self.ball.rect.x = self.ball.start_x
                        self.ball.rect.y = self.ball.start_y
                        self.ball.moving = False
                        return

    def speed_update(self):
        """
        vérifie si le bouton est toujours pressé et augmente la vitesse quand c'est le cas
        """
        button_pressed_time = Ball.handle_button_press(self.ball)
        if button_pressed_time is not None:
            self.ball.speed += get_shooting_speed(button_pressed_time)

    def run_game(self):
        pygame.init()
        pygame.display.set_caption("Tirs aux buts !")
        screen = pygame.display.set_mode((700, 460))
        background = pygame.image.load('assets/background.png')
        game = Game()
        running = True
        while running:
            if pygame.display.get_init():
                # vérifie si la fenêtre est ouverte car autrement il y a une erreur, même si elle impacte pas c'est mieux
                screen.blit(background, (0, 0))
                screen.blit(game.goal.image, game.goal.rect)
                screen.blit(game.ball.image_redimensionnee, game.ball.rect)
                self.quit_button.draw(screen)
                pygame.display.flip()
                game.handle_events()
                game.goal.move_ball()
                game.speed_update()
                game.update()
        pygame.quit()
