import pygame
import pygame_gui

# inicialização do pygame
pygame.init()

# estados do jogo
# criação de variáveis que não mudam (constantes) eu uso o padrão de tudo maiusculo
INICIO = 1
JOGANDO = 2
FIM = 3

# definir tamanhos
largura_tela = 800
altura_tela = 800
largura_snake = 40
altura_snake = 40
x_snake = largura_tela/2 - largura_snake/2
y_snake = altura_tela/2 - altura_snake/2

# criar a tela
screen = pygame.display.set_mode((largura_tela, altura_tela))

# criar o gerenciador do pygame_gui
gerente = pygame_gui.UIManager((largura_tela, altura_tela))

# criar o botão
botao_inicio = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((x_snake, y_snake), (100, 50)),
    text='Start Game',
    manager=gerente
)

# loop principal do jogo
running = True
estado = INICIO
while running:
    # percorrendo os eventos
    for event in pygame.event.get():
        # verificando se o evento é do tipo QUIT
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and estado == JOGANDO:
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
    if estado == JOGANDO:
        pygame.draw.rect(screen, (204, 153, 255), [(x_snake, y_snake), (largura_snake, altura_snake)])
    if estado == INICIO:
        gerente.update(1 / 60.0)
        gerente.draw_ui(screen)
    # atualizando a tela
    pygame.display.flip()
