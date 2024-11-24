import pygame
import time
from random import randint

pygame.init()

# Criando a janela do programa
back = (200, 255, 255)  # Cor de fundo
mw = pygame.display.set_mode((800, 600))  # Janela principal
mw.fill(back)
clock = pygame.time.Clock()

# Classe Rectangle
class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):  # Contorno de um retângulo existente
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

# Classe Label
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# Cores
RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)

# Configuração inicial
cards = []
num_cards = 4
card_width = 90
card_height = 100
spacing = 20  # Espaço entre os cartões

# Calculando a largura total ocupada pelos cartões e espaços
total_width = num_cards * card_width + (num_cards - 1) * spacing
start_x = (800 - total_width) // 2  # Centralizar horizontalmente na janela de 800px
start_y = (600 - card_height) // 2  # Centralizar verticalmente na janela de 600px

start_time = time.time()
cur_time = start_time

# Interface do jogo
time_text = Label(0, 0, 50, 50, back)
time_text.set_text('Time:', 40, DARK_BLUE)
time_text.draw(20, 20)

timer = Label(50, 55, 50, 40, back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0, 0)

score_text = Label(380, 0, 50, 50, back)
score_text.set_text('Count:', 45, DARK_BLUE)
score_text.draw(20, 20)

score = Label(430, 55, 50, 40, back)
score.set_text('0', 40, DARK_BLUE)
score.draw(0, 0)

# Criando os cartões
for i in range(num_cards):
    new_card = Label(start_x + i * (card_width + spacing), start_y, card_width, card_height, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card)

wait = 0
points = 0

# Loop principal
while True:
    # Desenhando os cartões e exibindo cliques
    if wait == 0:
        wait = 20  # Quantidade de ticks para manter o rótulo no mesmo lugar
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if (i + 1) == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1

    # Tratando cliques
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quando o botão "X" da janela é clicado
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x, y):
                    if i + 1 == click:  # Se há um rótulo no cartão, colore de verde e adiciona um ponto
                        cards[i].color(GREEN)
                        points += 1
                    else:  # Caso contrário, colore de vermelho e subtrai um ponto
                        cards[i].color(RED)
                        points -= 1
                    cards[i].fill()
                    score.set_text(str(points), 40, DARK_BLUE)
                    score.draw(0, 0)

    # Verificando vitória ou derrota
    new_time = time.time()

    if new_time - start_time >= 11:
        win = Label(0, 0, 500, 500, LIGHT_RED)
        win.set_text("Time is up!!!", 60, DARK_BLUE)
        win.draw(110, 180)
        pygame.display.update()

        # Mantendo a tela de derrota aberta
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    if int(new_time) - int(cur_time) == 1:  # Verifica diferença de 1 segundo entre os tempos
        timer.set_text(str(int(new_time - start_time)), 40, DARK_BLUE)
        timer.draw(0, 0)
        cur_time = new_time

    if points >= 5:
        win = Label(0, 0, 500, 500, LIGHT_GREEN)
        win.set_text("You won!!!", 60, DARK_BLUE)
        win.draw(140, 180)
        result_time = Label(90, 230, 250, 250, LIGHT_GREEN)
        result_time.set_text("Time to complete: " + str(int(new_time - start_time)) + " sec", 40, DARK_BLUE)
        result_time.draw(0, 0)
        pygame.display.update()

        # Mantendo a tela de vitória aberta
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    pygame.display.update()
    clock.tick(40)

pygame.display.update()
