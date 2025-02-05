print("~~~~~~~~~~-> CAMPO MINADO <-~~~~~~~~~~")
print("--------------------------------------")
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

