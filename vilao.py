from personagem import Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa um vilão no jogo.
    Herda da classe Personagem e adiciona atributos específicos.
    """
    def __init__(self, nome, vida, ataque, defesa, maldade):
        super().__init__(nome, vida, ataque, defesa)
        self.maldade = maldade

    def dialogar(self, outro_personagem):
        """
        Interação entre o vilão e outro personagem.
        """
        print(f'{self.nome}: "Você é fraco, {outro_personagem.nome}!"')
        print(f'{outro_personagem.nome}: "Eu vou te derrotar!"')

    def __str__(self):
        return f'{self.nome} (Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Maldade: {self.maldade})'