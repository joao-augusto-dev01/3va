import random
import os
import time

class Batalha:
    """
    Classe responsável por gerenciar batalhas entre heróis e vilões.
    """
    def __init__(self, heroi, vilao):
        self.heroi = heroi
        self.vilao = vilao

    def limpar_terminal(self):
        """
        Limpa o terminal.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_menu(self):
        """
        Exibe o menu de ações para o jogador.
        """
        print("\n=== MENU DE AÇÕES ===")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Usar Poção")
        print("4 - Dialogar")
        print("5 - Fugir")
        return input("Escolha uma ação (1-5): ")

    def evento_aleatorio(self):
        """
        Gera um evento aleatório durante a batalha.
        """
        eventos = [
            self.ataque_critico,
            self.vilao_se_cura,
            self.dialogo_inesperado
        ]
        evento_escolhido = random.choice(eventos)
        evento_escolhido()

    def ataque_critico(self):
        """
        O herói ou o vilão realiza um ataque crítico.
        """
        personagem = random.choice([self.heroi, self.vilao])
        dano = personagem.ataque * 2  # Dano dobrado
        alvo = self.vilao if personagem == self.heroi else self.heroi
        alvo.downgrade_vida(dano)
        print(f'⚡ {personagem.nome} realizou um ataque crítico e causou {dano} de dano!')

    def vilao_se_cura(self):
        """
        O vilão se cura durante a batalha.
        """
        cura = random.randint(10, 20)
        self.vilao.upgrade_vida(cura)
        print(f'💚 {self.vilao.nome} se curou em {cura} pontos de vida!')

    def dialogo_inesperado(self):
        """
        Um diálogo inesperado ocorre durante a batalha.
        """
        dialogos = [
            f'{self.heroi.nome}: "Você é mais forte do que eu pensava!"',
            f'{self.vilao.nome}: "Isso é tudo que você tem?"',
            f'{self.heroi.nome}: "Não vou desistir!"',
            f'{self.vilao.nome}: "Você nunca vai me derrotar!"'
        ]
        print(random.choice(dialogos))

    def iniciar(self):
        """
        Inicia uma batalha entre o herói e o vilão.
        Retorna o resultado da batalha.
        """
        print(f'=== BATALHA: {self.heroi.nome} vs {self.vilao.nome} ===')
        while self.heroi.vida > 0 and self.vilao.vida > 0:
            # Limpar o terminal
            self.limpar_terminal()

            # Mostrar status dos personagens
            print(f'\n{self.heroi.nome} (Vida: {self.heroi.vida}) vs {self.vilao.nome} (Vida: {self.vilao.vida})')

            # Jogador escolhe uma ação
            escolha = self.mostrar_menu()

            # Executar ação escolhida
            if escolha == "1":  # Atacar
                dano_heroi = max(self.heroi.ataque - self.vilao.defesa, 5)  # Dano mínimo de 5
                self.vilao.downgrade_vida(dano_heroi)
                print(f'{self.heroi.nome} atacou {self.vilao.nome} e causou {dano_heroi} de dano!')
            elif escolha == "2":  # Defender
                self.heroi.defesa += 5
                print(f'{self.heroi.nome} está defendendo! Defesa aumentada para {self.heroi.defesa}.')
            elif escolha == "3":  # Usar Poção
                self.heroi.usar_pocao()
            elif escolha == "4":  # Dialogar
                self.heroi.dialogar(self.vilao)
            elif escolha == "5":  # Fugir
                print(f'{self.heroi.nome} fugiu da batalha!')
                return "fugiu"
            else:
                print("Escolha inválida! Tente novamente.")
                continue

            # Pausa de 2 segundos para o jogador ler as mensagens
            time.sleep(2)

            # Verificar se o vilão foi derrotado
            if self.vilao.vida <= 0:
                return "heroi_venceu"

            # Evento aleatório
            if random.random() < 0.3:  # 30% de chance de ocorrer um evento
                self.evento_aleatorio()

            # Pausa de 2 segundos para o jogador ler as mensagens
            time.sleep(2)

            # Vilão ataca
            dano_vilao = max(self.vilao.ataque - self.heroi.defesa, 5)  # Dano mínimo de 5
            self.heroi.downgrade_vida(dano_vilao)
            print(f'{self.vilao.nome} atacou {self.heroi.nome} e causou {dano_vilao} de dano!')

            # Pausa de 2 segundos para o jogador ler as mensagens
            time.sleep(2)

        # Resultado da batalha
        if self.heroi.vida > 0 and self.vilao.vida <= 0:
            return "heroi_venceu"
        elif self.heroi.vida <= 0:
            return "vilao_venceu"
        else:
            return "fugiu"