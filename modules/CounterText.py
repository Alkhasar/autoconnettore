import pygame
from modules.Text import Text

class CounterText(Text):
    def __init__(self, screen, text, x, y):
        super().__init__(screen, text, x, y)
        self.counter = 0
    
    def update(self):
        self.textSurface = self.font.render(self.txt + str(self.counter), True, (20, 20, 20))
        super().update()
    
    def increment(self):
        self.counter += 1
