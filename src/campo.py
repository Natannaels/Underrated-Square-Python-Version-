import pygame

class Campo:
    def __init__(self, x, y, largura, altura, cor=(0,255,0)):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor

    def draw(self, tela):
        pygame.draw.rect(tela, (0, 168, 132), (self.x-2, self.y-2, self.largura+4, self.altura+4))
        return pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))