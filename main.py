import pygame

# inicialização do pygame
pygame.init()

# criar a tela
screen = pygame.display.set_mode((400, 400))

# loop principal do jogo
running = True
while running:
    # percorrendo os eventos
    for event in pygame.event.get():
        # verificando se o evento é do tipo QUIT
        if event.type == pygame.QUIT:
            running = False
    
    # pygame.draw.rect(screen, )