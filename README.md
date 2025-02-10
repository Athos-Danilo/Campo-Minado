Campo Minado - README
Este é um jogo de Campo Minado em Python. O objetivo é encontrar todas as minas ocultas no campo sem cair em nenhuma delas. O jogador pode escolher entre três níveis de dificuldade, cada um com diferentes tamanhos de campo e quantidade de minas.

Funcionalidades
Três níveis de dificuldade:

Fácil (9x9) com 10 minas.
Médio (16x16) com 40 minas.
Difícil (30x16) com 99 minas.
Marcação de minas: O jogador pode tentar marcar as minas que acredita estarem nas células, com a opção de marcar um local ao invés de escolher um para abrir.

Contagem de minas vizinhas: Para cada célula aberta, o jogo mostrará a quantidade de minas nas células ao redor, ajudando o jogador a deduzir onde as minas podem estar.

Fim de jogo: O jogo termina quando o jogador marca todas as minas corretamente, ou quando cai em uma mina. O número de tentativas também é mostrado ao final.

Como Jogar
Escolher o nível de dificuldade:

O jogo oferece três opções de nível: Fácil (9x9), Médio (16x16) e Difícil (30x16).
Abrir células:

O jogador deve escolher uma linha e uma coluna para tentar abrir uma célula. Se a célula não contiver uma mina, o número de minas ao redor será mostrado.
Marcar minas:

Quando o número de tentativas atinge 10, o jogador tem a opção de marcar uma célula com uma mina. Se a mina estiver no local correto, a célula é marcada com um "M". Se a marcação estiver errada, o jogo termina.
Ganhando o jogo:

O jogador vence ao marcar todas as minas corretamente ou ao abrir todas as células sem cair em uma mina.
Estrutura do Código
O código é dividido em funções para cada nível de dificuldade:

função facil():
Configura o jogo para o nível fácil (9x9, 10 minas).
função medio():
Configura o jogo para o nível médio (16x16, 40 minas).
função dificil():
Configura o jogo para o nível difícil (30x16, 99 minas).
Cada uma dessas funções cria um campo de minas, permite ao jogador interagir com o campo e verifica as escolhas feitas, com base nas coordenadas inseridas pelo jogador.

Como Executar:
1. Clone o repositório ou baixe o código.
2. Abra um terminal ou console.
3. Execute o código no Python 3.x:

python campo_minado.py

4. Siga as instruções no terminal para escolher o nível de dificuldade e jogar.