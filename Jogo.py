import random

def facil():
    linhas = 9
    colunas = 9
    matriz_facil = []
    tentativas = 1

    for contador_um in range(linhas):
        linha = []
        for contador_dois in range(colunas):
            linha.append("■")
        matriz_facil.append(linha)

    quantidade_facil = 10
    cordenadas = []
    for elementos_um in range(linhas):
        for elementos_dois in range(colunas):
            cordenadas.append((elementos_um, elementos_dois))
    facil_posicao = random.sample(cordenadas, quantidade_facil)

    minas = set(facil_posicao)

    def contador_de_minas(escolha_x, escolha_y, minas):
        contagem = 0
        minas_proximas = [(escolha_x, escolha_y-1), (escolha_x, escolha_y+1)]
        for cord_x, cord_y in minas_proximas:
            if 0 <= cord_y < colunas and (cord_x, cord_y) in minas:
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

    # repetição do jogo...
    
    print("--------------------------------------------")
    while True:
        try:
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
                    dica = contador_de_minas(escolha_x, escolha_y, minas)
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

# preciso fazer as dicas numericas 

print("")
print("~~~~~~~~~~~~-> \033[32m CAMPO MINADO \033[0m <-~~~~~~~~~~~~")
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



# criar inteface para como jogar o jogo

