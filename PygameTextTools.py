import pygame

class TextPrint:
    def __init__(self, x = 10, y = 10, line_height = 15, fontSize = 25):
        self.defaultX = x
        self.defaultY = y
        self.defaultLineLeight = line_height
        self.fontSize = fontSize
        self.font = pygame.font.Font(None, self.fontSize)
        self.indentSize = 10
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

    def indent(self):
        self.x += self.indentSize

    def unindent(self):
        self.x -= self.indentSize

class SimpleTextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 25)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10