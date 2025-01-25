import random

menor_numero = 1
maior_numero = 100
resposta = random.randint(menor_numero, maior_numero)
tentativas = 0 
esta_ocorrendo = True

print("Jogo de advinhar o numero em Python: ")
print(f"Escreva um número entre {menor_numero} e {maior_numero}")

while esta_ocorrendo:

    tentativa = input("Entre com o seu número: ")

    if tentativa.isdigit():
        tentativa = int(tentativa)
        tentativas += 1

        if tentativa < menor_numero or tentativa > maior_numero:
            print("Esse número não é valido")
            print(f"Por favor selecione um número entre entre {menor_numero} e {maior_numero}")

        elif tentativa < resposta:
            print("Esse número é menor que a respota. Tente novamente")
        elif tentativa > resposta:
            print("Esse número é maior que a respota. Tente novamente")
        else:
            print(f"Correto! O numero era {resposta}")
            print(f"A quantidade de tentativas foram {tentativas}")
            esta_ocorrendo = False
    else:
        print("Tentativa invalida")
        print(f"Por favor selecione um número entre entre {menor_numero} e {maior_numero}")
