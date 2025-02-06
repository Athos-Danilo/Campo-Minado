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


