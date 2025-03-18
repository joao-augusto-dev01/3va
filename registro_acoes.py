class RegistroAcoes:
    """
    Classe para registrar as ações do jogo.
    """
    def __init__(self):
        self.historico = []

    def registrar(self, acao):
        """
        Registra uma ação no histórico.
        """
        self.historico.append(acao)

    def exibir_historico(self):
        """
        Exibe o histórico de ações.
        """
        print("\n=== HISTÓRICO DE AÇÕES ===")
        for acao in self.historico:
            print(acao)