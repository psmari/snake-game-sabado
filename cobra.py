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
    
    def movimentar(self, key):
        if key == pygame.K_UP:
            self.y = self.y - 10
        if key == pygame.K_DOWN:
            self.y = self.y + 10
        if key == pygame.K_LEFT:
            self.x = self.x - 10
        if key == pygame.K_RIGHT:
            self.x = self.x + 10