import pygame
import pygame_gui

from cobra import Cobra

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

# instanciando a minha classe
cobra = Cobra(
    tamanho=40,
    cor=(204, 153, 255),
    x=largura_tela/2 - 40/2,
    y=altura_tela/2 - 40/2
)
# criar a tela
screen = pygame.display.set_mode((largura_tela, altura_tela))

# criar o gerenciador do pygame_gui
gerente = pygame_gui.UIManager((largura_tela, altura_tela))

# criar o botão
botao_inicio = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((cobra.x, cobra.y), (100, 50)),
    text='Start Game',
    manager=gerente
)

# loop principal do jogo
running = True
estado = INICIO
while running:
    # percorrendo os eventos
    for event in pygame.event.get():
        gerente.process_events(event)
        # verificando se o evento é do tipo QUIT
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and estado == JOGANDO:
            cobra.movimentar(event.key)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == botao_inicio:
                estado = JOGANDO
        
    # limpando a tela            
    screen.fill((0, 0, 0))
    if estado == JOGANDO:
        cobra.aparecer(screen)
    if estado == INICIO:
        gerente.update(1 / 60.0)
        gerente.draw_ui(screen)
    # atualizando a tela
    pygame.display.flip()
