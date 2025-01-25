#Classe do Player onde vai ser colocado o seu Nome(nickname) e seu código 
class Jogador:

    def __init__(self: object, nome: str, codigo) -> None:
        self.codigo = codigo
        self.nome: str = nome
        self.pontuacao = 0
    
    def salvar_nome(self):
        with open(self.nome_arquivo, "w") as file:
            file.write(self.codigo)
            file.write(self.nome)

    def atualizar_placar(self):
        try:
            with open("placar.txt", "a") as file:
                file.write(f"{self.codigo},{self.nome},{self.pontuacao}\n")
        except OSError as e:
            print(f"Erro ao atualizar o placar: {e}")