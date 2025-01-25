#Jogo Quiz Python

questoes = ("Quantos elesmentos existem na tabela periodica? ",
            "Qual animal bota os maiores ovos? ",
            "Qual é o gas mais abundante no planeta terra? ",
            "Quantos ossos existem no corpo humano adulto? ",
            "Qual é o platena mais quente do sistema solar? ")

opcoes = (("A. 116", "B. 117", "C. 118", "D. 119"), 
          ("A. Baleia", "B. Crocodilo", "C. Elefante", "D. Avestruz"), 
          ("A. Nitrogenio", "B. Oxigenio", "C. Dioxido de carbono", "D. Hidrogenio"), 
          ("A. 206", "B. 207", "C. 208", "D. 209"), 
          ("A. Mercurio", "B. venus", "C. Terra", "D. Marte"))

respostas = ("C", "D", "A", "A", "B")
Tentativas = []
pontuacao = 0 
questao_numero = 0

for questoe in questoes:
    print("----------------")
    print(questoe)
    for opcao in opcoes[questao_numero]:
        print(opcao)
        
    Tentativa = input("Entre com (A,B,C,D): ").upper()
    Tentativas.append(Tentativa)
    if Tentativa == respostas[questao_numero]:
        pontuacao += 1
        print("ACERTOU")
    else:
        print("ERROU")
        print(f"{respostas[questao_numero]} é a reposta correta")
    questao_numero += 1
print("----------------")
print("    Resultado   ")
print("----------------")

print("Resposta ", end=" ")
for resposta in respostas:
    print(resposta, end=" ")
print()

print("Tentativa ", end=" ")
for tentativa in Tentativas:
    print(tentativa, end=" ")
print()

pontuacao = int(pontuacao / len(questoes) * 100)
print(f"Sua pontuação é de {pontuacao}%")