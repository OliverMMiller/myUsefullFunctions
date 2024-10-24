import pygame

class TextPrint:
    def __init__(self, x = 10, y = 10, line_height = 15, fontSize = 25):
        self.defaultX = x
        self.defaultY = y
        self.defaultLineLeight = line_height
        self.fontSize = fontSize
        self.font = pygame.font.Font(None, self.fontSize)
        self.textColor = (0, 0, 0)
        self.backgroundColor = None #(255, 255, 255)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, self.textColor, self.backgroundColor)
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = self.defaultX
        self.y = self.defaultY
        self.line_height = self.defaultLineLeight