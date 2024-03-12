import pygame
class Button:
    def __init__(self, color, x, y, width, height, text=' '):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text

    def draw (self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        if self.text != '':
            font = pygame.font.Font(None, 50)
            text=font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

