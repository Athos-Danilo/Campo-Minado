def facil():
    linhas = 9 
    colunas = 9
    matriz_facil = []
    for contador in range(linhas):
        linha = []
    for contador in range(colunas):
        linha.append(0)
    matriz_facil.append(linha)

print("")
print("~~~~~~~~~~~~-> \033[32m CAMPO MINADO \033[0m <-~~~~~~~~~~~~")
print("--------------------------------------------")
print("ESCOLHA O NÍVEL DE DIFICULDADE:")
print("[1] Fácil")
print("[2] Médio")
print("[3] Difícil")
while True:
    try:
        nivel = int(input(": "))
        if nivel in [1, 2, 3]:
            break
        else:
            print("Só existem três níveis! Digite 1, 2 ou 3.")
    except ValueError:
        print("Digite um Número Válido!")




