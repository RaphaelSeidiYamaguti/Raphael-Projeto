"""
Estudo dirigido do primeiro Bimestre

Alunos:
Raphael Seidi Yamaguti
Gabriel Felix Silva
"""

from time import sleep

from models.player import Jogador
from models.jogo import Jogo


def main() -> None:
    menu()

#Menu do Jogo
def menu() -> None:
    print('===========================================')
    print('============== JOGO DA FORCA ==============')
    print('===========================================')

    print('1 - Novo Jogo')
    print('2 - Continuar')
    print('3 - Placar')
    print('4 - Sair')

    opcao: int = int(input())

    if opcao == 1:
        novo_jogo()
    elif opcao == 2:
        continuar_jogo()
    elif opcao == 3:
        placar()
    elif opcao == 4:
        exit()
    else:
        print('Essa opção não existe tente novamante...')
        sleep(1)
        menu()

def novo_jogo():
    print("Começando um jogo novo")
    comeco: str = input("Você quer criar um novo jogo? S/N ").upper()
    if comeco == 'S':
        jogo = Jogo()
        jogador = criar_jogador()
        jogo.novo_jogo(jogador)
    elif comeco == 'N':
        sleep(2)
        menu()
    else:
        print("Não existe essa opção voltando ao menu")
        sleep(2)
        menu()

def criar_jogador():
    nome = input("Digite o seu nome: ")
    codigo = input("Digite o código do jogador: ")
    return Jogador (nome,codigo)

def continuar_jogo():
    print("Continuando um novo jogo")
    continua: str = input("Você quer continuar um jogo? S/N ").upper()
    if continua == 'S':
        jogo = Jogo()
        codigo_jogador = input("Digite o código do jogador: ")
        jogador = Jogador("", codigo_jogador)
        jogo.continuar_com_jogador(jogador)
    elif continua == 'N':
        sleep(2)
        menu()
    else:
        print("Não existe essa opção voltando ao menu")
        sleep(2)
        menu()


def placar():
    print("========= Placar do Jogo =========")
    print("Código | Nome do Jogador | Pontuação")
    with open("placar.txt", 'r') as f:
        for linha in f:
            dados = linha.strip().split(',')
            if len(dados) == 3:
                codigo, nome, pontuacao = dados
                print(f"{codigo:^7} | {nome:^15} | {pontuacao:^10}")
    sleep(1)
    menu()

if __name__ == '__main__':
    main()