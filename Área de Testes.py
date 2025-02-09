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

import random

def facil():
    linhas = 9
    colunas = 9
    matriz_facil = []

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
    
    for coordenada_x, coordenada_y in facil_posicao:
        matriz_facil[coordenada_x][coordenada_y] = "X"

    print("    ",end="")
    for contador_tres in range(colunas):
        print(f"{contador_tres} ", end="")
    print()    
    
    for contador_quatro, linha in enumerate(matriz_facil):
        print(f"{contador_quatro} > ", end="")
        for elemento in linha:
            print(elemento, end=' ')
        print() 

    # preciso fazer a parte do usuario escolher a localização!
    
    print("--------------------------------------------")
    while True:
        try:
            escolha_x = int(input("Selecione a LINHA (0 a 8): "))
            escolha_y = int(input("Selecione a COLUNA (0 a 8): "))
            if 0 <= escolha_x <= 8 and 0 <= escolha_y <= 8:
                if matriz_facil[escolha_x][escolha_y] == "X":
                    print("Perdeu!")
                    break
                else:
                    matriz_facil[escolha_x][escolha_y] = "#"
                    for contador_quatro, linha in enumerate(matriz_facil):
                        print(f"{contador_quatro} > ", end="")
                        for elemento in linha:
                            print(elemento, end=' ')
                        print()  
            else:
                print("Coordenadas inválidas, tente novamente.")
        except ValueError:
            print("Apenas Números Inteiros!")

# 2. preciso fazer com que as minas fiquem escondidas 
# 1. preeciso modificar a parte de escolher a localização para que quando o usuario selecione um elemento ele mude para outra forma
# 3.

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


