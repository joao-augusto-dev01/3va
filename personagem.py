class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.defesa_base = defesa  # Valor base de defesa para resetar após defesa
        self.energia = 100  # Energia para habilidades especiais

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem.
        """
        self.vida += incremento
        print(f'Vida de {self.nome} aumentou para {self.vida}.')

    def downgrade_vida(self, decremento):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        if self.vida > decremento:
            self.vida -= decremento
            print(f'{self.nome} perdeu {decremento} de vida! Vida restante: {self.vida}')
        else:
            self.vida = 0
            print(f'{self.nome} foi derrotado!')

    def reset_defesa(self):
        """
        Reseta a defesa para o valor base.
        """
        self.defesa = self.defesa_base
        print(f'Defesa de {self.nome} resetada para {self.defesa}.')

    def esta_vivo(self):
        """
        Verifica se o personagem ainda está vivo.
        """
        return self.vida > 0

    def status(self):
        """
        Exibe o status completo do personagem.
        """
        print(f'\n=== STATUS DE {self.nome.upper()} ===')
        print(f'Vida: {self.vida}')
        print(f'Ataque: {self.ataque}')
        print(f'Defesa: {self.defesa}')
        print(f'Energia: {self.energia}')

    def __str__(self):
        return f'{self.nome} (Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa})'