import random

opcoes = ("pedra", "papel", "tesoura")

ocorrendo = True

while ocorrendo:

    jogador = None
    computador = random.choice(opcoes)

    while jogador not in opcoes:
        jogador = input("Selecione (Pedra, Papel, Tesoura): ").lower()

    print(f"Jogador: {jogador}")
    print(f"Computador: {computador}")

    if jogador == computador:
        print("É um empate!")
    elif jogador == "pedra" and computador == "tesoura":
        print("Você Ganhou!!")
    elif jogador == "papel" and computador == "pedra":
        print("Você Ganhou!!")
    elif jogador == "tesoura" and computador == "papel":
        print("Você Ganhou!!")
    else:
        print("Você Perdeu!!")

    if not input("Quer jogar novamente (S/N)").lower() == 's':
        ocorrendo = False

print("Obrigado por Jogar!!!")
