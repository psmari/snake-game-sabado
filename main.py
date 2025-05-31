import pygame

# inicialização do pygame
pygame.init()

# definir tamanhos
largura_tela = 800
altura_tela = 800
largura_snake = 40
altura_snake = 40
x_snake = largura_tela/2 - largura_snake/2
y_snake = altura_tela/2 - altura_snake/2

# criar a tela
screen = pygame.display.set_mode((largura_tela, altura_tela))
print('Numero do evento KEYDOWN', pygame.KEYDOWN)
# loop principal do jogo
running = True
while running:
    # percorrendo os eventos
    for event in pygame.event.get():
        # verificando se o evento é do tipo QUIT
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_snake = y_snake - 10
            if event.key == pygame.K_DOWN:
                y_snake = y_snake + 10
            if event.key == pygame.K_LEFT:
                x_snake = x_snake - 10
            if event.key == pygame.K_RIGHT:
                x_snake = x_snake + 10
    
    # limpando a tela            
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (204, 153, 255), [(x_snake, y_snake), (largura_snake, altura_snake)])
    # atualizando a tela
    pygame.display.flip()
