import pygame

class Cobra:
    def __init__(self, tamanho, cor, x, y):
        self.tamanho = tamanho
        self.cor = cor
        self.x = x
        self.y = y
    
    def aparecer(self, screen):
        pygame.draw.rect(
            screen,
            self.cor,
            ((self.x, self.y), (self.tamanho, self.tamanho))
        )