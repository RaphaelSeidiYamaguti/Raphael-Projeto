#Biblioteca random para randomizar as palavras do jogo da forca
from models.player import Jogador
import random

#Classe do jogo
class Jogo():

    def __init__(self: object) -> None:
        self.chances:int = 6
        self.jogador = Jogador
        self.nome_arquivo = ""
        self.letras_erradas = []
        self.letras_corretas = []
        self.palavra = ""
    
    def escolher_palavra(self):
        palavras = ["python", "comida", "amigo", "abacaxi", "aviao", "anel", "aventura", "alegria", "abelha", "assado", "almofada", "agricultor",
            "brinquedo", "borboleta", "bussola", "beisebol", "castelo", "cozinha", "cachoeira", "ciclismo", "corrida", "carangueijo",
              "diamante", "divertido", "elefante", "energia", "estante", "entusiasmo", "escorregador", "futebol", "fantoche", "fotografia", 
              "fechadura", "felicidade"]
        return random.choice(palavras)
    
    
    def solicitar_codigo_jogador(self):
        self.codigo_jogador = input("Digite o código do jogador para continuar o jogo: ")
        self.nome_arquivo = f"{self.codigo_jogador}_save.txt"

    def continuar_com_jogador(self, jogador):
        self.jogador = jogador
        self.solicitar_codigo_jogador()
        try:
            with open(self.nome_arquivo, "r") as file:
                self.jogador.nome = file.readline().strip()
                self.palavra = file.readline().strip()
                self.letras_erradas = file.readline().strip().split()
                self.letras_corretas = file.readline().strip().split()
                tentativas_str = file.readline().strip()
                self.tentativas = int(tentativas_str) if tentativas_str.isdigit() else 0
                if self.jogador:
                    self.jogo_carregado()
                
        except FileNotFoundError:
            print("Nenhum jogo salvo encontrado.")
    def jogo_carregado(self):
        self.nome_arquivo = f"{self.jogador.codigo}_save.txt"
        self.letras_erradas = []
        self.letras_corretas = []
        self.palavra = self.escolher_palavra()
        self.quantidade_letras = len(self.palavra)
        self.numero = int(self.quantidade_letras)
        self.chances = 6
        if self.jogador:
            self.jogar()
        

    def novo_jogo(self, jogador):
        self.jogador = jogador
        self.nome_arquivo = f"{self.jogador.codigo}_save.txt"
        self.letras_erradas = []
        self.letras_corretas = []
        self.palavra = self.escolher_palavra()
        self.quantidade_letras = len(self.palavra)
        self.numero = int(self.quantidade_letras)
        self.chances = 6
        if self.jogador:
            self.atribuir_pontos()
            self.jogar()
        else:
            print("Erro ao criar jogador")

    def jogo(self):
        
        self.nome_arquivo = f"{self.jogador.codigo}_save.txt"
        self.letras_erradas = []
        self.letras_corretas = []
        self.palavra = self.escolher_palavra()
        self.quantidade_letras = len(self.palavra)
        self.numero = int(self.quantidade_letras)
        self.chances = 6
        if self.jogador:
            self.atribuir_pontos()
            self.jogar()

    def salvar_jogo(self):
        with open(self.nome_arquivo, "w") as file:
            file.write("Nome: "+ self.jogador.nome + "\n")
            file.write("Codigo: " + self.jogador.codigo + "\n")
            file.write("Palavra: " + self.palavra + "\n")
            file.write("Letras Erradas: " + " ".join(self.letras_erradas) + "\n")
            file.write(" ".join(self.letras_corretas) + "\n")
            file.write("Chances: "+ str(self.chances) + "\n")

    
    def atribuir_pontos(self):
        comprimento_palavra = len(self.palavra)
        if comprimento_palavra >= 4 and comprimento_palavra <= 6:
            print("Você ganhou 1 ponto")
            self.jogador.pontuacao += 1
        elif comprimento_palavra >= 7 and comprimento_palavra <= 9:
            print("Você ganhou 2 pontos")
            self.jogador.pontuacao += 2
        elif comprimento_palavra > 9:
            print("Você ganhou 3 pontos")
            self.jogador.pontuacao += 3

    def jogar(self: object) -> None:
        fim_jogo = False

        while not fim_jogo:
            self.mostrar_palavra()
            print("Letras erradas:", " ".join(self.letras_erradas))
            print(f"Você tem {self.chances} chances")

            # Verifica se o jogador ganhou
            if all(letra in self.letras_corretas for letra in self.palavra):
                print("Parabéns, você venceu!")
                opcao = input("Deseja jogar novamente? S= JogarNovamente N= SalvarJogo ").upper()
                if opcao != 'S':
                    self.jogador.atualizar_placar()
                    self.salvar_jogo()      
                    exit()
                else:
                    self.jogo()
                

            # Verifica se o jogador perdeu
            if self.chances == 0:
                print("Você perdeu! A palavra era:", self.palavra)
                opcao = input("Deseja jogar novamente? (S/N) ").upper()
                if opcao == 'S':
                    self.novo_jogo()
                else:
                    self.jogador.atualizar_placar()
                    fim_jogo = True

           
            letra = input("Digite uma letra: ").lower()

            if letra in self.palavra:
                self.letras_corretas.append(letra)
            else:
                self.letras_erradas.append(letra)
                self.chances -= 1

    def jogar2(self: object) -> None:
        self.jogo()
            

    def mostrar_palavra(self):
        for letra in self.palavra:
            if letra in self.letras_corretas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print()
    
                    
        

