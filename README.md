# Jogo de Batalha: Herói vs Vilão

Este é um jogo de batalha em texto desenvolvido em Python, onde o jogador controla um herói que deve derrotar um vilão para salvar a Princesa Zelda. O jogo inclui um sistema de turnos, eventos aleatórios e uma interface simples para escolher ações.

## Funcionalidades

- **Batalha por Turnos**: O jogador escolhe ações como atacar, defender, usar poção, dialogar ou fugir.
- **Eventos Aleatórios**: Durante a batalha, eventos aleatórios podem ocorrer, como ataques críticos, cura do vilão ou diálogos inesperados.
- **Objetivo**: Derrotar o vilão para salvar a Princesa Zelda. Se o herói perder, o vilão mata a princesa.
- **Interface Simples**: O jogo é executado no terminal, com mensagens claras e pausas para facilitar a leitura.

## Como Executar o Jogo

### Pré-requisitos

- Python 3.x instalado no seu sistema.

### Passos para Executar

1. Clone o repositório (se aplicável):

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Execute o jogo:

   ```bash
   python main.py
   ```

3. Siga as instruções:

   - Durante a batalha, você verá um menu de ações. Escolha uma opção digitando o número correspondente.
   - O jogo informará o resultado de cada ação e o estado atual da batalha.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

```
/
|-- main.py            # Arquivo principal que inicia o jogo
|-- heroi.py           # Contém a classe Heroi, que herda de Personagem
|-- vilao.py           # Contém a classe Vilao, que herda de Personagem
|-- personagem.py      # Classe base Personagem com atributos comuns
|-- batalha.py         # Classe que gerencia a lógica da batalha
|-- registro_acoes.py  # Classe que registra o histórico de ações
```

## Classes Principais

### Personagem

#### Atributos:

- `nome`: Nome do personagem.
- `vida`: Pontos de vida do personagem.
- `ataque`: Poder de ataque do personagem.
- `defesa`: Poder de defesa do personagem.

#### Métodos:

- `upgrade_vida(incremento)`: Aumenta a vida do personagem.
- `downgrade_vida(decremento)`: Reduz a vida do personagem.
- `__str__()`: Retorna uma representação textual do personagem.

### Heroi (Herda de Personagem)

#### Métodos Adicionais:

- `salvar_refem()`: Salva um refém e recupera vida.
- `usar_pocao()`: Usa uma poção para recuperar vida.
- `dialogar(outro_personagem)`: Inicia um diálogo com outro personagem.

### Vilao (Herda de Personagem)

#### Atributos Adicionais:

- `maldade`: Nível de maldade do vilão.

#### Métodos Adicionais:

- `dialogar(outro_personagem)`: Inicia um diálogo com outro personagem.

### Batalha

#### Métodos:

- `iniciar()`: Inicia a batalha entre o herói e o vilão.
- `evento_aleatorio()`: Gera um evento aleatório durante a batalha.
- `mostrar_menu()`: Exibe o menu de ações para o jogador.

### RegistroAcoes

#### Métodos:

- `registrar(acao)`: Registra uma ação no histórico.
- `exibir_historico()`: Exibe o histórico de ações.

## Exemplo de Jogabilidade

### Início do Jogo:

```
=== BATALHA: Link vs Ganon ===

Link (Vida: 100) vs Ganon (Vida: 120)

=== MENU DE AÇÕES ===
1 - Atacar
2 - Defender
3 - Usar Poção
4 - Dialogar
5 - Fugir
Escolha uma ação (1-5): 1
```

### Ação do Jogador:

```
Link atacou Ganon e causou 15 de dano!
```

### Evento Aleatório:

```
⚡ Link realizou um ataque crítico e causou 30 de dano!
```

### Resultado da Batalha:

```
🎉 Link venceu a batalha e salvou a Princesa Zelda! 🎉
```
