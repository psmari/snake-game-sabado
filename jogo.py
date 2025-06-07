import pygame 
import pygame_gui
from cobra import Cobra

class Jogo:
    def __init__(self):
        # inicialização do pygame
        pygame.init()
        
        # estados do jogo
        # criação de variáveis que não mudam (constantes) eu uso o padrão de tudo maiusculo
        self.INICIO = 1
        self.JOGANDO = 2
        self.FIM = 3

        # definir tamanhos
        self.largura_tela = 800
        self.altura_tela = 800

        # criar a tela
        self.screen = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        
        # criar o gerenciador do pygame_gui
        self.gerente = pygame_gui.UIManager((self.largura_tela, self.altura_tela))

        self.center_y = self.altura_tela/2 - 40/2
        self.center_x= self.largura_tela/2 - 40/2
        
        # criar o botão
        self.botao_inicio = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.center_x, self.center_y), (100, 50)),
            text='Start Game',
            manager=self.gerente
        )
        
        self.running = True
        self.estado = self.INICIO
          
    def atualizar_tela(self):
        self.screen.fill((0, 0, 0))
    
    def controlar_eventos(self, cobra):
        # percorrendo os eventos
        for event in pygame.event.get():
            self.gerente.process_events(event)
            # verificando se o evento é do tipo QUIT
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and self.estado == self.JOGANDO:
                cobra.movimentar(event.key)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.botao_inicio:
                    self.estado = self.JOGANDO
    
    def mostrar_menu(self):
        self.gerente.update(1 / 60.0)
        self.gerente.draw_ui(self.screen)
    
    def mostrar_jogo(self, cobra):
        cobra.aparecer(self.screen)
    
    def executar(self):
        # instanciando a minha classe cobra
        cobra = Cobra(
            tamanho=40,
            cor=(204, 153, 255),
            x=self.largura_tela/2 - 40/2,
            y=self.altura_tela/2 - 40/2
        )

        # loop principal do jogo
        while self.running:
            self.controlar_eventos(cobra)
            
            self.atualizar_tela()
                       
            if self.estado == self.JOGANDO:
                self.mostrar_jogo(cobra)
            if self.estado == self.INICIO:
                self.mostrar_menu()
            
            pygame.display.flip()