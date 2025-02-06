def facil():
    linhas = 9
    colunas = 9
    matriz_facil = []

    for contador_um in range(linhas):
        linha = []
        for contador_dois in range(colunas):
            linha.append("■")
        matriz_facil.append(linha)

    print("    ",end="")
    for contador_tres in range(colunas):
        print(f"{contador_tres}", end="")
    print()    
    
    # for linha in matriz_facil:
    #     for elemento in linha:
    #         print(elemento, end=' ')
    #     print() 

print("")
print("~~~~~~~~~~~~-> \033[32m CAMPO MINADO \033[0m <-~~~~~~~~~~~~")
print("--------------------------------------------")
print("ESCOLHA O NÍVEL DE DIFICULDADE:")
print("[1] Fácil")
print("[2] Médio")
print("[3] Difícil")
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

