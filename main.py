from heroi import Heroi
from vilao import Vilao
from batalha import Batalha
from registro_acoes import RegistroAcoes

def main():
    registro = RegistroAcoes()

    # Criando heróis e vilões
    heroi = Heroi('Link', 100, 20, 15)
    vilao = Vilao('Ganon', 120, 25, 10, 'Alta')

    # Estado inicial da Princesa Zelda
    princesa_zelda = "em perigo"

    # Diálogo inicial
    heroi.dialogar(vilao)
    registro.registrar(f'{heroi.nome} e {vilao.nome} iniciaram um diálogo.')

    # Batalha
    batalha = Batalha(heroi, vilao)
    resultado = batalha.iniciar()
    registro.registrar(f'{heroi.nome} e {vilao.nome} batalharam.')

    # Verificar o resultado da batalha
    if resultado == "heroi_venceu":
        princesa_zelda = "salva"
        print(f'\n🎉 {heroi.nome} venceu a batalha e salvou a Princesa Zelda! 🎉')
    elif resultado == "vilao_venceu":
        princesa_zelda = "morta"
        print(f'\n💀 {vilao.nome} venceu a batalha e matou a Princesa Zelda! 💀')
    else:
        print(f'\n{heroi.nome} fugiu da batalha. A Princesa Zelda continua em perigo.')

    # Exibir histórico
    registro.exibir_historico()

if __name__ == "__main__":
    main()