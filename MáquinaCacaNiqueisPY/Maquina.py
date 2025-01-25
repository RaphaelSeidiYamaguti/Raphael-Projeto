#Máquina Caça Niqueis em Python
import random

def girar_linha():
    simbolos = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(simbolos) for _ in range(3)]

def print_linha(girar):
    print("**************")
    print(" | ".join(girar))
    print("**************")

def pegar_payout(girar, apostar):
    if girar[0] == girar[1] == girar[2]:
        if girar[0] == '🍒':
            return apostar * 3
        elif girar[0] == '🍉':
            return apostar * 4
        elif girar[0] == '🍋':
            return apostar * 5
        elif girar[0] == '🔔':
            return apostar * 10
        elif girar[0] == '⭐':
            return apostar * 20
    return 0
        

def main():
    dinheiro = 100
    print("****************************************")
    print("Seja Bem Vindo a Máquina Caça Niqueis!!!")
    print("****** Simbolos: 🍒 🍉 🍋 🔔 ⭐ ******")
    print("****************************************")

    while dinheiro > 0:
        print(f"Você ainda tem {dinheiro}R$ ")

        apostar = input("Coloque a quantidade que você deseja apostar: ")

        if not apostar.isdigit():
            print("Por favor, utiliza um valor válido. ")
            continue

        apostar = int(apostar)

        if apostar > dinheiro:
            print("Você não tem dinheiro o suficiente para apostar")
            continue

        if apostar <= 0:
            print("A aposta precisa ser maior que 0")
            continue

        dinheiro -= apostar

        girar = girar_linha()
        print("Girando...\n")
        print_linha(girar)

        payout = pegar_payout(girar, apostar)

        if payout >0: 
            print(f"Você Ganhou {payout}R$")
        else:
            print("Você perdeu")
        
        dinheiro += payout

        jogar_novamente = input("Você quer jogar novamente? (S/N) ").upper()
        if jogar_novamente != 'S':
            break
    
    print("*********************************************************")
    print(f"O jogo terminou, você ficou com um total de {dinheiro}R$")
    print("*********************************************************")

if __name__ == '__main__':
    main()