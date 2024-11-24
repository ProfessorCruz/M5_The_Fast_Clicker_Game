'''
'''
import pygame
import time
from random import randint

pygame.init()

# Criando a janela do programa com fundo claro
back = (200, 255, 255)  # Cor de fundo
mw = pygame.display.set_mode((800, 600))  # Janela principal com tamanho 800x600
mw.fill(back)  # Preenche a tela com a cor de fundo
clock = pygame.time.Clock()  # Controla a taxa de atualização do jogo

# Classe que define uma área retangular
class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  # Define a posição e tamanho do retângulo
        self.fill_color = color  # Cor de preenchimento

    def color(self, new_color):
        self.fill_color = new_color  # Modifica a cor de preenchimento do retângulo

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)  # Desenha o retângulo preenchido

    def outline(self, frame_color, thickness):  # Contorno do retângulo
        pygame.draw.rect(mw, frame_color, self.rect, thickness)  # Desenha o contorno

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)  # Verifica se o ponto (x, y) está dentro do retângulo

# Classe Label, que herda da classe Area, usada para criar texto em caixas
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)  # Renderiza o texto

    def draw(self, shift_x=0, shift_y=0):
        self.fill()  # Preenche a área com a cor de fundo
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  # Desenha o texto na tela

# Cores definidas para o jogo
RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)

# Configuração inicial do jogo
cards = []  # Lista que vai armazenar os cartões
num_cards = 4  # Número de cartões
card_width = 90  # Largura de cada cartão
card_height = 100  # Altura de cada cartão
spacing = 20  # Espaçamento entre os cartões

# Calculando a largura total ocupada pelos cartões e espaços, e centralizando na tela
total_width = num_cards * card_width + (num_cards - 1) * spacing
start_x = (800 - total_width) // 2  # Centraliza horizontalmente
start_y = (600 - card_height) // 2  # Centraliza verticalmente

# Inicia o tempo do jogo
start_time = time.time()  # Hora de início
cur_time = start_time  # Variável de controle do tempo

# Interface do jogo - Labels para exibir informações
time_text = Label(0, 0, 50, 50, back)
time_text.set_text('Time:', 40, DARK_BLUE)
time_text.draw(20, 20)  # Exibe o texto 'Time:'

# Timer: Exibe o tempo decorrido
timer = Label(150, 21, 50, 40, back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0, 0)

# Score Text: Exibe o texto 'Count:'
score_text = Label(380, 0, 50, 50, back)
score_text.set_text('Count:', 45, DARK_BLUE)
score_text.draw(20, 20)

# Score: Exibe a pontuação
score = Label(560, 24, 50, 40, back)
score.set_text('0', 40, DARK_BLUE)
score.draw(0, 0)

# Criando os cartões
for i in range(num_cards):
    # Adiciona um cartão à lista de cartões
    new_card = Label(start_x + i * (card_width + spacing), start_y, card_width, card_height, YELLOW)
    new_card.outline(BLUE, 10)  # Adiciona um contorno ao cartão
    new_card.set_text('CLICK', 26)  # Texto padrão do cartão
    cards.append(new_card)  # Adiciona o cartão à lista de cartões

wait = 0  # Variável de controle de tempo para mudança dos cartões
points = 0  # Inicializa a pontuação

# Loop principal do jogo
while True:
    # Desenha os cartões e exibe o clique
    if wait == 0:
        wait = 20  # Quantidade de ticks para manter o rótulo no mesmo lugar
        click = randint(1, num_cards)  # Define aleatoriamente qual cartão será destacado
        for i in range(num_cards):
            cards[i].color(YELLOW)  # Todos os cartões ficam amarelos
            if (i + 1) == click:
                cards[i].draw(10, 40)  # Cartão destacado
            else:
                cards[i].fill()  # Outros cartões são desenhados sem texto
    else:
        wait -= 1  # Diminui o tempo de espera para a mudança do destaque

    # Tratamento dos eventos de clique
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fechar a janela
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos  # Pega a posição do clique
            for i in range(num_cards):
                if cards[i].collidepoint(x, y):  # Verifica se o clique foi em algum cartão
                    if i + 1 == click:  # Se o cartão correto foi clicado
                        cards[i].color(GREEN)  # Marca como acerto (verde)
                        points += 1  # Incrementa a pontuação
                    else:  # Se o cartão errado foi clicado
                        cards[i].color(RED)  # Marca como erro (vermelho)
                        points -= 1  # Decrementa a pontuação
                    cards[i].fill()  # Atualiza o cartão
                    score.set_text(str(points), 40, DARK_BLUE)  # Atualiza a pontuação
                    score.draw(0, 0)

    # Atualiza o tempo na interface
    elapsed_time = int(time.time() - start_time)  # Calcula o tempo decorrido desde o início
    timer.set_text(str(elapsed_time), 40, DARK_BLUE)  # Atualiza o timer
    timer.draw(0, 0)

    # Verificando vitória ou derrota
    new_time = time.time()  # Pega o tempo atual

    # Se o tempo se esgotar ou a pontuação atingir 5 pontos, termina o jogo
    if new_time - start_time >= 11 or points >= 5:
        is_victory = points >= 5 and points > 0  # Define vitória apenas se a pontuação for maior que 0
        bg_color = LIGHT_GREEN if is_victory else LIGHT_RED  # Cor de fundo de vitória ou derrota
        message = "You won!!!" if is_victory else "Time is up!!!"  # Mensagem final

        # Criar tela de fundo
        win = Label(0, 0, 800, 600, bg_color)
        win.fill()

        # Posições e espaçamento para as mensagens
        text_x = 220  # Posição horizontal
        base_y = 180  # Posição vertical
        line_spacing = 70  # Espaçamento entre as linhas

        # Mensagem principal
        main_message = Label(0, 0, 800, 100, bg_color)
        main_message.set_text(message, 60, DARK_BLUE)
        main_message.draw(text_x, base_y)

        # Exibe a pontuação final
        final_score = Label(0, 0, 800, 100, bg_color)
        final_score.set_text(f"Final Score: {points}", 50, DARK_BLUE)
        final_score.draw(text_x, base_y + line_spacing)

        # Exibe o tempo total
        result_time = Label(0, 0, 800, 100, bg_color)
        result_time.set_text(f"Time to complete: {int(new_time - start_time)} sec", 40, DARK_BLUE)
        result_time.draw(text_x, base_y + 2 * line_spacing)

        pygame.display.update()

        # Mantém a tela de vitória ou derrota aberta até o usuário fechar a janela
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    pygame.display.update()  # Atualiza a tela
    clock.tick(40)  # Controla a taxa de atualização

    pygame.display.update() 
