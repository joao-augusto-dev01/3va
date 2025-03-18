from personagem import Personagem

class Heroi(Personagem):
    """
    A classe Heroi representa um herói no jogo.
    Herda da classe Personagem e adiciona métodos específicos.
    """
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.pocoes = 3  # Número de poções disponíveis

    def salvar_refem(self):
        """
        O herói salva um refém, ganhando pontos de vida.
        """
        self.upgrade_vida(20)
        print(f'{self.nome} salvou um refém e recuperou 20 de vida!')

    def usar_pocao(self):
        """
        O herói usa uma poção para recuperar vida.
        """
        if self.pocoes > 0:
            self.upgrade_vida(30)
            self.pocoes -= 1
            print(f'{self.nome} usou uma poção e recuperou 30 de vida! Poções restantes: {self.pocoes}')
        else:
            print(f'{self.nome} não tem mais poções!')

    def dialogar(self, outro_personagem):
        """
        Interação entre o herói e outro personagem.
        """
        print(f'{self.nome}: "Você não vai escapar, {outro_personagem.nome}!"')
        print(f'{outro_personagem.nome}: "Você nunca me pegará!"')