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





def facil():
    linhas = 9
    colunas = 9
    matriz_facil = []
    for contador in range(linhas):
        linha = []
        for contador in range(colunas):
            linha.append(0)
        matriz_facil.append(linha)
    return matriz_facil
print(facil())
