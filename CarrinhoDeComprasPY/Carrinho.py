#Carrinho de Compra em Python

comidas = [ ]
precos = [ ]
total = 0

while True:
    comida = input("Entre com uma comida que você quer comprar: (q para sair)")
    if comida.lower() == "q":
        break
    else:
        preco = float(input(f"Entre com o valor da {comida}: R$")) 
        comidas.append(comida)
        precos.append(preco)

print("-----Seu Carrinho-----")

for comida in comidas:
    print(comida, end=" ")

for preco in precos:
    total += preco

print()
print(f"Seu total foi de: R${total}")