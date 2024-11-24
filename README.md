# Jogo de Cartões - Projeto da Algorithmics Programming School

Este é um jogo simples desenvolvido como parte do curso da **Algorithmics Programming School**, atualizado por **Reneé Cruz**. O objetivo do jogo é clicar no cartão correto que aparece destacado na tela, acumulando pontos. O tempo é limitado e a pontuação é determinada pelos acertos ou erros durante o jogo.

## Descrição

O jogo apresenta um conjunto de cartões dispostos na tela. Um dos cartões será destacado aleatoriamente, e o jogador deve clicar nesse cartão. A cada acerto, a pontuação aumenta, e a cada erro, a pontuação diminui. O jogo termina quando o tempo se esgota ou o jogador alcança uma pontuação de 5 pontos.

### Funcionalidades:
- **Cartões Aleatórios**: Um cartão aleatório é destacado em cada rodada e o jogador deve clicar nele.
- **Pontuação**: O jogador ganha 1 ponto por acerto e perde 1 ponto por erro.
- **Temporizador**: O jogo tem um limite de tempo de 11 segundos.
- **Tela de Vitória/Derrota**: Ao final, o jogador é informado se venceu ou perdeu, com a exibição da pontuação final e o tempo gasto.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do jogo.
- **Pygame**: Biblioteca utilizada para criar a interface gráfica e gerenciar a lógica do jogo.

## Instruções de Uso

### Pré-requisitos:
- Python 3.x
- Pygame (pode ser instalado via `pip`)

### Como Rodar o Jogo:
1. Clone este repositório:
   git clone https://github.com/ProfessorCruz/M5_The_Fast_Clicker_Game

2. Instale as dependências necessárias:
    pip install pygame

3. Execute o jogo:
    python jogo_cartoes.py

O jogo será iniciado em uma janela gráfica onde você poderá interagir com os cartões. Clique no cartão correto para ganhar pontos e veja a contagem de tempo e pontuação sendo atualizadas.

### Estrutura do Código:
jogo_cartoes.py: Arquivo principal do jogo, contendo a lógica e a interface gráfica.
Classes:
    Area: Representa uma área retangular na tela, com métodos para desenhar e interagir com ela.
    Label: Extende a classe Area e adiciona a funcionalidade de exibir textos na tela.
    Cartões: São objetos da classe Label, representando os cartões do jogo.
Variáveis:
    cards: Lista que armazena os objetos Label representando os cartões.
    points: Controla a pontuação do jogador.
    start_time: Marca o início do tempo de jogo.

### Contribuições
Este projeto foi desenvolvido como parte do curso da Algorithmics Programming School e foi atualizado pelo professor desta mesma escola: Reneé Cruz.
Contribuições são bem-vindas, sinta-se à vontade para fazer um fork deste repositório e propor melhorias!

### Licença
Este projeto é licenciado sob a MIT License.

### Agradecimentos
Agradecemos a Algorithmics Programming School pela base do projeto, que serviu como ponto de partida para este desenvolvimento.

