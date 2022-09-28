# Importing pygame
import pygame

class Button():
    """Sono pigro non mi va di commentare ma è un pulsante...
    ┻━┻︵ \(°□°)/ ︵ ┻━┻
    """
    def __init__(self, screen, x, y, w, h, defTxt, txtOnClick, onClickFx=None, toggleble=True):
        # Standard initialization
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.defTxt = defTxt
        self.onClickFx = onClickFx
        self.txtOnClick = txtOnClick
        self.state = False
        self.pressed = False
        self.font = pygame.font.SysFont("Arial Black", 20)
        self.screen = screen

        # Fill Colors
        self.fillColors = {
            "idle": "#325c19",
            "hover": "#7bce4b",
            "pressed": "#4b97ce",
        }

        # Creating surface and rect
        self.surface = pygame.Surface((self.w, self.h))
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.txtA = self.font.render(self.defTxt, True, (20, 20, 20))
        self.txtB = self.font.render(self.txtOnClick, True, (20, 20, 20))
    
    def update(self):
        mousePosition = pygame.mouse.get_pos()
        self.surface.fill(self.fillColors["idle"])
        if(self.rect.collidepoint(mousePosition)):
            self.surface.fill(self.fillColors["hover"])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.surface.fill(self.fillColors["hover"])
                if not self.pressed:
                    self.onClickFx()
                    self.state = not self.state
                    self.pressed = True

            else:
                self.pressed = False

        if self.state:
            self.surface.blit(self.txtB, [
                self.rect.width/2 - self.txtB.get_rect().width/2,
                self.rect.height/2 - self.txtB.get_rect().height/2
            ])
        else:
            self.surface.blit(self.txtA, [
                self.rect.width/2 - self.txtA.get_rect().width/2,
                self.rect.height/2 - self.txtA.get_rect().height/2
            ])

        self.screen.blit(self.surface, self.rect)