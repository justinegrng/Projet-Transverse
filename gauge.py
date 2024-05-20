import pygame
from trajectory import Trajectory


class Gauge:
    def __init__(self, color, x, y, width, height):
        self.trajectory = Trajectory()
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.width_gauge = self.width

    def draw(self, screen):
        self.trajectory.update_strike_force()
        self.width_gauge = (self.trajectory.strike_force - 76) * 20
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width_gauge, self.height))
