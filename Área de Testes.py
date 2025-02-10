# Área de testes...

# facil = [
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8]
# ]


# for linha in facil:
#     print(linha)

# facil[2][5] = 0

# print("")

# for linha in facil:
#     for elemento in linha:
#         print(elemento, end=' ')
#     print()





# def facil():
#     linhas = 9
#     colunas = 9
#     matriz_menor = []

#     for contador_um in range(linhas):
#         linha = []
#         for contador_dois in range(colunas):
#             linha.append(0)
#         matriz_menor.append(linha)

#     return matriz_menor

# matriz_facil = facil()

# for linha in matriz_facil:
#     for elemento in linha:
#         print(elemento, end=' ')
#     print()    


# def facil():
#     linhas = 9
#     colunas = 9
#     matriz_menor = []

#     for contador_um in range(linhas):
#         linha = []
#         for contador_dois in range(colunas):
#             linha.append("■")
#         matriz_menor.append(linha)
        
#     for linha in matriz_menor:
#         for elemento in linha:
#             print(elemento, end=' ')
#         print()    

# facil()

# def facil():
#     linhas = 9
#     colunas = 9
#     matriz_menor = [["■"] * colunas for _ in range(linhas)]  # Criando a matriz de forma compacta

#     # Exibir números das colunas (cabeçalho)
#     print("   " + " ".join(f"{j}" for j in range(colunas)))  

#     # Exibir matriz com números das linhas (índice)
#     for i, linha in enumerate(matriz_menor):
#         print(f"{i} | " + " ".join(linha))

# # Chamar a função
# facil()


# def facil():
#     linhas = 9
#     colunas = 9
#     matriz_menor = []
    
#     # Criação da matriz
#     for contador_um in range(linhas):
#         linha = []
#         for contador_dois in range(colunas):
#             linha.append("■")
#         matriz_menor.append(linha)
    
#     # Imprimir os números das colunas
#     print("    ", end="")
#     for i in range(colunas):
#         print(f"{i} ", end="")
#     print()  # Pular uma linha após os números das colunas
    
#     # Imprimir a matriz com os números das linhas
#     for i, linha in enumerate(matriz_menor):
#         print(f"{i} | ", end="")  # Número da linha à esquerda
#         for elemento in linha:
#             print(elemento, end=' ')
#         print()  # Quebra de linha após cada linha da matriz

# # Chama a função
# facil()

# import random

# def facil():
#     linhas = 9
#     colunas = 9
#     matriz_facil = []

#     for contador_um in range(linhas):
#         linha = []
#         for contador_dois in range(colunas):
#             linha.append("■")
#         matriz_facil.append(linha)

#     quantidade_facil = 10
#     cordenadas = []
#     for elementos_um in range(linhas):
#         for elementos_dois in range(colunas):
#             cordenadas.append((elementos_um, elementos_dois))
#     facil_posicao = random.sample(cordenadas, quantidade_facil)
    
#     for coordenada_x, coordenada_y in facil_posicao:
#         matriz_facil[coordenada_x][coordenada_y] = "X"

#     print("    ",end="")
#     for contador_tres in range(colunas):
#         print(f"{contador_tres} ", end="")
#     print()    
    
#     for contador_quatro, linha in enumerate(matriz_facil):
#         print(f"{contador_quatro} > ", end="")
#         for elemento in linha:
#             print(elemento, end=' ')
#         print() 

#     # preciso fazer a parte do usuario escolher a localização!
    
#     print("--------------------------------------------")
#     while True:
#         try:
#             escolha_x = int(input("Selecione a LINHA (0 a 8): "))
#             escolha_y = int(input("Selecione a COLUNA (0 a 8): "))
#             if 0 <= escolha_x <= 8 and 0 <= escolha_y <= 8:
#                 if matriz_facil[escolha_x][escolha_y] == "X":
#                     print("Perdeu!")
#                     break
#                 else:
#                     matriz_facil[escolha_x][escolha_y] = "#"
#                     for contador_quatro, linha in enumerate(matriz_facil):
#                         print(f"{contador_quatro} > ", end="")
#                         for elemento in linha:
#                             print(elemento, end=' ')
#                         print()  
#             else:
#                 print("Coordenadas inválidas, tente novamente.")
#         except ValueError:
#             print("Apenas Números Inteiros!")

# # 2. preciso fazer com que as minas fiquem escondidas 
# # 1. preeciso modificar a parte de escolher a localização para que quando o usuario selecione um elemento ele mude para outra forma
# # 3.

# print("")
# print("~~~~~~~~~~~~-> \033[32m CAMPO MINADO \033[0m <-~~~~~~~~~~~~")
# print("--------------------------------------------")
# print("ESCOLHA O NÍVEL DE DIFICULDADE:")
# print("[1] Fácil --> (9x9)")
# print("[2] Médio --> (16x16)")
# print("[3] Difícil --> (30x16)")
# while True:
#     try:
#         nivel = int(input("Resposta: "))
#         if nivel in [1, 2, 3]:
#             break
#         else:
#             print("Só existem três níveis! Digite 1, 2 ou 3.")
#     except ValueError:
#         print("Digite um Número Válido!")
# print("--------------------------------------------")
# if nivel == 1:
#     facil()


# import random

# def facil():
#     linhas = 9
#     colunas = 9
#     matriz_facil = []
#     tentativas = 1

#     for _ in range(linhas):
#         linha = []
#         for _ in range(colunas):
#             linha.append("■")
#         matriz_facil.append(linha)

#     quantidade_facil = 10
#     coordenadas = [(i, j) for i in range(linhas) for j in range(colunas)]
#     facil_posicao = random.sample(coordenadas, quantidade_facil)
#     minas = set(facil_posicao)

#     # Função para contar minas ao redor
#     def contar_minas_ao_redor(x, y, minas):
#         direcoes = [(-1, -1), (-1, 0), (-1, 1),
#                     (0, -1),          (0, 1),
#                     (1, -1),  (1, 0), (1, 1)]
#         contador = 0
#         for dx, dy in direcoes:
#             novo_x, novo_y = x + dx, y + dy
#             if 0 <= novo_x < linhas and 0 <= novo_y < colunas:
#                 if (novo_x, novo_y) in minas:
#                     contador += 1
#         return contador

#     # Impressão inicial do tabuleiro
#     print("    ", end="")
#     for contador_tres in range(colunas):
#         print(f"{contador_tres} ", end="")
#     print()

#     for contador_quatro, linha in enumerate(matriz_facil):
#         print(f"{contador_quatro} > ", end="")
#         for elemento in linha:
#             print(elemento, end=' ')
#         print()

#     # Repetição do jogo
#     print("--------------------------------------------")
#     while True:
#         try:
#             escolha_x = int(input("Selecione a LINHA (0 a 8): "))
#             escolha_y = int(input("Selecione a COLUNA (0 a 8): "))
#             if 0 <= escolha_x <= 8 and 0 <= escolha_y <= 8:
#                 if (escolha_x, escolha_y) in minas:
#                     print("\033[31mPerdeu! Você caiu numa Mina :( \033[0m")
#                     print(f"\033[31mNúmero de Tentativas: {tentativas}\033[0m")
#                     for posicao_x, posicao_y in minas:
#                         matriz_facil[posicao_x][posicao_y] = "\033[31mX\033[0m"
#                     print("--------------------------------------------")
#                     print("    ", end="")
#                     for contador_tres in range(colunas):
#                         print(f"{contador_tres} ", end="")
#                     print()
#                     for contador_quatro, linha in enumerate(matriz_facil):
#                         print(f"{contador_quatro} > ", end="")
#                         for elemento in linha:
#                             print(elemento, end=' ')
#                         print()
#                     print("--------------------------------------------")
#                     break
#                 else:
#                     dica = contar_minas_ao_redor(escolha_x, escolha_y, minas)
#                     if dica == 0:
#                         matriz_facil[escolha_x][escolha_y] = "\033[32m#\033[0m"
#                     else:
#                         matriz_facil[escolha_x][escolha_y] = f"\033[34m{dica}\033[0m"
#                     tentativas += 1

#                     print("--------------------------------------------")
#                     print("    ", end="")
#                     for contador_tres in range(colunas):
#                         print(f"{contador_tres} ", end="")
#                     print()

#                     for contador_quatro, linha in enumerate(matriz_facil):
#                         print(f"{contador_quatro} > ", end="")
#                         for elemento in linha:
#                             print(elemento, end=' ')
#                         print()
#             else:
#                 print("Coordenadas inválidas, tente novamente.")
#         except ValueError:
#             print("Apenas Números Inteiros!")
#         print("--------------------------------------------")

# # Menu inicial
# print("")
# print("~~~~~~~~~~~~-> \033[32m CAMPO MINADO \033[0m <-~~~~~~~~~~~~")
# print("--------------------------------------------")
# print("ESCOLHA O NÍVEL DE DIFICULDADE:")
# print("[1] Fácil --> (9x9)")
# print("[2] Médio --> (16x16)")
# print("[3] Difícil --> (30x16)")
# while True:
#     try:
#         nivel = int(input("Resposta: "))
#         if nivel in [1, 2, 3]:
#             break
#         else:
#             print("Só existem três níveis! Digite 1, 2 ou 3.")
#     except ValueError:
#         print("Digite um Número Válido!")
# print("--------------------------------------------")
# if nivel == 1:
#     facil()



# import random

# def facil():
#     linhas = 9
#     colunas = 9
#     matriz_facil = []
#     tentativas = 1

#     for contador_um in range(linhas):
#         linha = []
#         for contador_dois in range(colunas):
#             linha.append("■")
#         matriz_facil.append(linha)

#     quantidade_facil = 10
#     cordenadas = []
#     for elementos_um in range(linhas):
#         for elementos_dois in range(colunas):
#             cordenadas.append((elementos_um, elementos_dois))
#     facil_posicao = random.sample(cordenadas, quantidade_facil)

#     minas = set(facil_posicao)

#     def contador_de_minas(escolha_x, escolha_y, minas):
#         contagem = 0
#         minas_perto = [(x,y-1), (x, y+1)]

#     print("    ",end="")
#     for contador_tres in range(colunas):
#         print(f"{contador_tres} ", end="")
#     print()    
    
#     for contador_quatro, linha in enumerate(matriz_facil):
#         print(f"{contador_quatro} > ", end="")
#         for elemento in linha:
#             print(elemento, end=' ')
#         print() 

#     # repetição do jogo...
    
#     print("--------------------------------------------")
#     while True:
#         try:
#             escolha_x = int(input("Selecione a LINHA (0 a 8): "))
#             escolha_y = int(input("Selecione a COLUNA (0 a 8): "))
#             if 0 <= escolha_x <= 8 and 0 <= escolha_y <= 8:
#                 if (escolha_x, escolha_y) in minas:
#                     print("\033[31mPerdeu! Você caiu numa Mina :( \033[0m ")
#                     print(f"\033[31mNúmero de Tentativas: {tentativas}\033[0m")
#                     for posicao_x, posicao_y in minas:
#                         matriz_facil[posicao_x][posicao_y] = "\033[31mX\033[0m"
#                     print("--------------------------------------------")
#                     print("    ", end="")
#                     for contador_tres in range(colunas):
#                         print(f"{contador_tres} ", end="")
#                     print()
#                     for contador_quatro, linha in enumerate(matriz_facil):
#                         print(f"{contador_quatro} > ", end="")
#                         for elemento in linha:
#                             print(elemento, end=' ')
#                         print()
#                     print("--------------------------------------------")
#                     break
#                 else:
#                     matriz_facil[escolha_x][escolha_y] = "\033[32m#\033[0m"
#                     tentativas += 1
#                     print("--------------------------------------------")
#                     print("    ",end="")
#                     for contador_tres in range(colunas):
#                         print(f"{contador_tres} ", end="")
#                     print()
                    
#                     for contador_quatro, linha in enumerate(matriz_facil):
#                         print(f"{contador_quatro} > ", end="")
#                         for elemento in linha:
#                             print(elemento, end=' ')
#                         print()
#             else:
#                 print("Coordenadas inválidas, tente novamente.")
#         except ValueError:
#             print("Apenas Números Inteiros!")
#         print("--------------------------------------------")

# # preciso fazer as dicas numericas 

# print("")
# print("~~~~~~~~~~~~-> \033[32m CAMPO MINADO \033[0m <-~~~~~~~~~~~~")
# print("--------------------------------------------")
# print("ESCOLHA O NÍVEL DE DIFICULDADE:")
# print("[1] Fácil --> (9x9)")
# print("[2] Médio --> (16x16)")
# print("[3] Difícil --> (30x16)")
# while True:
#     try:
#         nivel = int(input("Resposta: "))
#         if nivel in [1, 2, 3]:
#             break
#         else:
#             print("Só existem três níveis! Digite 1, 2 ou 3.")
#     except ValueError:
#         print("Digite um Número Válido!")
# print("--------------------------------------------")
# if nivel == 1:
#     facil()




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











