# Importing pygame
import pygame

class Text:
    def __init__(self, screen, text, x, y):
        """Build a text object and adds it to screen

        Args:
            screen (pygame.screen): main screen used to draw stuff
            text (string): text to render
            x (int): horizontal position of topleft rect corner
            y (int): vertical position of topleft rect corner
        """
        # Standard initialization
        self._x = x
        self.x = 0
        self.y = y
        self.txt = text
        self.screen = screen

        # Font
        self.font = pygame.font.SysFont("Arial Black", 10)
        
        self.changeText(self.txt)

    def update(self):
        """Automatically called to update every object
        """
        self.screen.blit(self.textSurface, [self.x, self.y])

    def changeText(self, text):
        """Used to dynamically change text and reset position

        Args:
            text (string): text to render
        """
        # Setting text
        self.txt = text

        # Text
        self.textSurface = self.font.render(self.txt, True, (20, 20, 20))

        # Centering TEXT
        self.x = self._x - self.textSurface.get_rect().width/2 