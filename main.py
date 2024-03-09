import pygame
from goal import*
from game import Game
pygame.init()

pygame.display.set_caption("Penalty game")
screen = pygame.display.set_mode((700,460))

background = pygame.image.load('assets/background.png')

game = Game()

running = True

while running:

    screen.blit(background, (0, 0))

    screen.blit(game.goal.image, game.goal.rect)

    screen.blit(game.ball.image_redimensionnee, game.ball.rect)

    pygame.display.flip()

    game.handle_events()

    game.goal.move_ball()

    game.update()

if __name__ == "__main__":
    run_game()