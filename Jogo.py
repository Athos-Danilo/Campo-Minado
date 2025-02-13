import random

def facil():
    linhas = 9
    colunas = 9
    matriz_facil = []
    tentativas = 1
    marcacoes = set()

    for contador_um in range(linhas):
        linha = []
        for contador_dois in range(colunas):
            linha.append("■")
        matriz_facil.append(linha)

    quantidade_facil = 10
    coordenadas = []
    for elementos_um in range(linhas):
        for elementos_dois in range(colunas):
            coordenadas.append((elementos_um, elementos_dois))
    facil_posicao = random.sample(coordenadas, quantidade_facil)

    minas = set(facil_posicao)

    def contador_de_minas(escolha_x, escolha_y):
        contagem = 0
        minas_proximas = [
            (escolha_x, escolha_y -1),
            (escolha_x, escolha_y +1)
        ]
        for direcao_x, direcao_y in minas_proximas:
            if 0 <= direcao_x < linhas and 0 <= direcao_y < colunas and (direcao_x, direcao_y) in minas:
                contagem += 1
        return contagem

    print("    ",end="")
    for contador_tres in range(colunas):
        print(f"{contador_tres} ", end="")
    print()    
    
    for contador_quatro, linha in enumerate(matriz_facil):
        print(f"{contador_quatro} > ", end="")
        for elemento in linha:
            print(elemento, end=' ')
        print() 
    
    print("--------------------------------------------")
    while True:
        try:
            if tentativas >= 10:
                resposta = input("Deseja Marcar uma Mina? (SIM / 'Enter' -> Continuar): ").lower()
                if resposta == "sim":
                    marcar_x = int(input("Informe a Linha da Mina: "))
                    marcar_y = int(input("Informe a Coluna da Mina: "))
                    if (marcar_x, marcar_y) in minas:
                        print("\033[32mParabéns! Você marcou uma mina corretamente!\033[0m")
                        matriz_facil[marcar_x][marcar_y] = "\033[35mM\033[0m"
                        marcacoes.add((marcar_x, marcar_y))
                        if marcacoes == minas:
                            print("\033[32mVocê marcou todas as Minas corretamente! Você venceu o Jogo!\033[0m")
                            break
                    else:
                        print("\033[31mErrou! Voceê marcou Errado a Mina.\033[0m")
                        break
                    continue

            escolha_x = int(input("Selecione a LINHA (0 a 8): "))
            escolha_y = int(input("Selecione a COLUNA (0 a 8): "))
            if 0 <= escolha_x <= 8 and 0 <= escolha_y <= 8:
                if (escolha_x, escolha_y) in minas:
                    print("\033[31mPerdeu! Você caiu numa Mina :( \033[0m ")
                    print(f"\033[31mNúmero de Tentativas: {tentativas}\033[0m")
                    for posicao_x, posicao_y in minas:
                        matriz_facil[posicao_x][posicao_y] = "\033[31mX\033[0m"
                    print("--------------------------------------------")
                    print("    ", end="")
                    for contador_tres in range(colunas):
                        print(f"{contador_tres} ", end="")
                    print()
                    for contador_quatro, linha in enumerate(matriz_facil):
                        print(f"{contador_quatro} > ", end="")
                        for elemento in linha:
                            print(elemento, end=' ')
                        print()
                    print("--------------------------------------------")
                    break
                else:
                    dica = contador_de_minas(escolha_x, escolha_y)
                    if dica == 0:
                        matriz_facil[escolha_x][escolha_y] = "\033[32m#\033[0m"
                    else:
                        matriz_facil[escolha_x][escolha_y] = f"\033[34m{dica}\033[0m"
                    tentativas += 1
                    print("--------------------------------------------")
                    print("    ",end="")
                    for contador_tres in range(colunas):
                        print(f"{contador_tres} ", end="")
                    print()
                    
                    for contador_quatro, linha in enumerate(matriz_facil):
                        print(f"{contador_quatro} > ", end="")
                        for elemento in linha:
                            print(elemento, end=' ')
                        print()
            else:
                print("Coordenadas inválidas, tente novamente.")
        except ValueError:
            print("Apenas Números Inteiros!")
        print("--------------------------------------------")


def medio():
    linhas = 16
    colunas = 16
    matriz_facil = []
    tentativas = 1
    marcacoes = set()

    for contador_um in range(linhas):
        linha = []
        for contador_dois in range(colunas):
            linha.append("■")
        matriz_facil.append(linha)

    quantidade_facil = 40
    coordenadas = []
    for elementos_um in range(linhas):
        for elementos_dois in range(colunas):
            coordenadas.append((elementos_um, elementos_dois))
    facil_posicao = random.sample(coordenadas, quantidade_facil)

    minas = set(facil_posicao)

    def contador_de_minas(escolha_x, escolha_y):
        contagem = 0
        minas_proximas = [
            (escolha_x, escolha_y -1),
            (escolha_x, escolha_y +1)
        ]
        for direcao_x, direcao_y in minas_proximas:
            if 0 <= direcao_x < linhas and 0 <= direcao_y < colunas and (direcao_x, direcao_y) in minas:
                contagem += 1
        return contagem

    print("    ",end="")
    for contador_tres in range(colunas):
        print(f"{contador_tres}", end=" ")
    print()    
    
    for contador_quatro, linha in enumerate(matriz_facil):
        print(f"{contador_quatro} >  ", end="")
        for elemento in linha:
            print(elemento, end=' ')
        print() 

    
    print("--------------------------------------------")
    while True:
        try:
            if tentativas >= 10:
                resposta = input("Deseja Marcar uma Mina? (SIM / 'Enter' -> Continuar): ").lower()
                if resposta == "sim":
                    marcar_x = int(input("Informe a Linha da Mina: "))
                    marcar_y = int(input("Informe a Coluna da Mina: "))
                    if (marcar_x, marcar_y) in minas:
                        print("\033[32mParabéns! Você marcou uma mina corretamente!\033[0m")
                        matriz_facil[marcar_x][marcar_y] = "\033[35mM\033[0m"
                        marcacoes.add((marcar_x, marcar_y))
                        if marcacoes == minas:
                            print("\033[32mVocê marcou todas as Minas corretamente! Você venceu o Jogo!\033[0m")
                            break
                    else:
                        print("\033[31mErrou! Voceê marcou Errado a Mina.\033[0m")
                        break
                    continue

            escolha_x = int(input("Selecione a LINHA (0 a 15): "))
            escolha_y = int(input("Selecione a COLUNA (0 a 15): "))
            if 0 <= escolha_x <= 15 and 0 <= escolha_y <= 15:
                if (escolha_x, escolha_y) in minas:
                    print("\033[31mPerdeu! Você caiu numa Mina :( \033[0m ")
                    print(f"\033[31mNúmero de Tentativas: {tentativas}\033[0m")
                    for posicao_x, posicao_y in minas:
                        matriz_facil[posicao_x][posicao_y] = "\033[31mX\033[0m"
                    print("--------------------------------------------")
                    print("    ", end="")
                    for contador_tres in range(colunas):
                        print(f"{contador_tres} ", end="")
                    print()
                    for contador_quatro, linha in enumerate(matriz_facil):
                        print(f"{contador_quatro} > ", end="")
                        for elemento in linha:
                            print(elemento, end=' ')
                        print()
                    print("--------------------------------------------")
                    break
                else:
                    dica = contador_de_minas(escolha_x, escolha_y)
                    if dica == 0:
                        matriz_facil[escolha_x][escolha_y] = "\033[32m#\033[0m"
                    else:
                        matriz_facil[escolha_x][escolha_y] = f"\033[34m{dica}\033[0m"
                    tentativas += 1
                    print("--------------------------------------------")
                    print("    ",end="")
                    for contador_tres in range(colunas):
                        print(f"{contador_tres} ", end="")
                    print()
                    
                    for contador_quatro, linha in enumerate(matriz_facil):
                        print(f"{contador_quatro} > ", end="")
                        for elemento in linha:
                            print(elemento, end=' ')
                        print()
            else:
                print("Coordenadas inválidas, tente novamente.")
        except ValueError:
            print("Apenas Números Inteiros!")
        print("--------------------------------------------")


def dificil():
    linhas = 30
    colunas = 16
    matriz_facil = []
    tentativas = 1
    marcacoes = set()

    for contador_um in range(linhas):
        linha = []
        for contador_dois in range(colunas):
            linha.append("■")
        matriz_facil.append(linha)

    quantidade_facil = 99
    coordenadas = []
    for elementos_um in range(linhas):
        for elementos_dois in range(colunas):
            coordenadas.append((elementos_um, elementos_dois))
    facil_posicao = random.sample(coordenadas, quantidade_facil)

    minas = set(facil_posicao)

    def contador_de_minas(escolha_x, escolha_y):
        contagem = 0
        minas_proximas = [
            (escolha_x, escolha_y -1),
            (escolha_x, escolha_y +1)
        ]
        for direcao_x, direcao_y in minas_proximas:
            if 0 <= direcao_x < linhas and 0 <= direcao_y < colunas and (direcao_x, direcao_y) in minas:
                contagem += 1
        return contagem

    print("    ",end="")
    for contador_tres in range(colunas):
        print(f"{contador_tres} ", end="")
    print()    
    
    for contador_quatro, linha in enumerate(matriz_facil):
        print(f"{contador_quatro} > ", end="")
        for elemento in linha:
            print(elemento, end=' ')
        print() 

    
    
    print("--------------------------------------------")
    while True:
        try:
            if tentativas >= 10:
                resposta = input("Deseja Marcar uma Mina? (SIM / 'Enter' -> Continuar): ").lower()
                if resposta == "sim":
                    marcar_x = int(input("Informe a Linha da Mina: "))
                    marcar_y = int(input("Informe a Coluna da Mina: "))
                    if (marcar_x, marcar_y) in minas:
                        print("\033[32mParabéns! Você marcou uma mina corretamente!\033[0m")
                        matriz_facil[marcar_x][marcar_y] = "\033[35mM\033[0m"
                        marcacoes.add((marcar_x, marcar_y))
                        if marcacoes == minas:
                            print("\033[32mVocê marcou todas as Minas corretamente! Você venceu o Jogo!\033[0m")
                            break
                    else:
                        print("\033[31mErrou! Voceê marcou Errado a Mina.\033[0m")
                        break
                    continue

            escolha_x = int(input("Selecione a LINHA (0 a 29): "))
            escolha_y = int(input("Selecione a COLUNA (0 a 15): "))
            if 0 <= escolha_x <= 29 and 0 <= escolha_y <= 15:
                if (escolha_x, escolha_y) in minas:
                    print("\033[31mPerdeu! Você caiu numa Mina :( \033[0m ")
                    print(f"\033[31mNúmero de Tentativas: {tentativas}\033[0m")
                    for posicao_x, posicao_y in minas:
                        matriz_facil[posicao_x][posicao_y] = "\033[31mX\033[0m"
                    print("--------------------------------------------")
                    print("    ", end="")
                    for contador_tres in range(colunas):
                        print(f"{contador_tres} ", end="")
                    print()
                    for contador_quatro, linha in enumerate(matriz_facil):
                        print(f"{contador_quatro} > ", end="")
                        for elemento in linha:
                            print(elemento, end=' ')
                        print()
                    print("--------------------------------------------")
                    break
                else:
                    dica = contador_de_minas(escolha_x, escolha_y)
                    if dica == 0:
                        matriz_facil[escolha_x][escolha_y] = "\033[32m#\033[0m"
                    else:
                        matriz_facil[escolha_x][escolha_y] = f"\033[34m{dica}\033[0m"
                    tentativas += 1
                    print("--------------------------------------------")
                    print("    ",end="")
                    for contador_tres in range(colunas):
                        print(f"{contador_tres} ", end="")
                    print()
                    
                    for contador_quatro, linha in enumerate(matriz_facil):
                        print(f"{contador_quatro} > ", end="")
                        for elemento in linha:
                            print(elemento, end=' ')
                        print()
            else:
                print("Coordenadas inválidas, tente novamente.")
        except ValueError:
            print("Apenas Números Inteiros!")
        print("--------------------------------------------")
 

print("")
print("~~~~~~~~~~~~-> \033[32m CAMPO MINADO \033[0m <-~~~~~~~~~~~~")
print("--------------------------------------------")
print("------[1] Iniciar ----- [2] Saiba Mais -----")
while True:
    try:
        iniciar = int(input("Resosta: "))
        if iniciar in [1, 2]:
            break
        else:
            print("Só existem duas opções! Digite 1 ou 2.")
    except ValueError:
        print("Digite um Número Válido!")
if iniciar == 1:
    print("ESCOLHA O NÍVEL DE DIFICULDADE:")
    print("[1] Fácil --> (9x9)")
    print("[2] Médio --> (16x16)")
    print("[3] Difícil --> (30x16)")
    while True:
        try:
            nivel = int(input("Resposta: "))
            if nivel in [1, 2, 3]:
                break
            else:
                print("Só existem três níveis! Digite 1, 2 ou 3.")
        except ValueError:
            print("Digite um Número Válido!")
    print("--------------------------------------------")
    if nivel == 1:
        facil()
    elif nivel == 2:
        medio()
    elif nivel == 3:
        dificil()
elif iniciar == 2:
    print("--------------------------------------------")
    print(
        "Escolha a Dificuldade do jogo, no nível fácil tem 10 Minas, no Médio 40 Minas e no Difícil 99 Minas."
        "\n" "Para Ganhar você precisa achar todas as Minas."
    )
    print("--------------------------------------------")
    print("ESCOLHA O NÍVEL DE DIFICULDADE:")
    print("[1] Fácil --> (9x9)")
    print("[2] Médio --> (16x16)")
    print("[3] Difícil --> (30x16)")
    while True:
        try:
            nivel = int(input("Resposta: "))
            if nivel in [1, 2, 3]:
                break
            else:
                print("Só existem três níveis! Digite 1, 2 ou 3.")
        except ValueError:
            print("Digite um Número Válido!")
    print("--------------------------------------------")
    if nivel == 1:
        facil()
    elif nivel == 2:
        medio()
    elif nivel == 3:
        dificil()


