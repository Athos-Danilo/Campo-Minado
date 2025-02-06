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


def facil():
    linhas = 9
    colunas = 9
    matriz_menor = []
    
    # Criação da matriz
    for contador_um in range(linhas):
        linha = []
        for contador_dois in range(colunas):
            linha.append("■")
        matriz_menor.append(linha)
    
    # Imprimir os números das colunas
    print("    ", end="")
    for i in range(colunas):
        print(f"{i} ", end="")
    print()  # Pular uma linha após os números das colunas
    
    # Imprimir a matriz com os números das linhas
    for i, linha in enumerate(matriz_menor):
        print(f"{i} | ", end="")  # Número da linha à esquerda
        for elemento in linha:
            print(elemento, end=' ')
        print()  # Quebra de linha após cada linha da matriz

# Chama a função
facil()