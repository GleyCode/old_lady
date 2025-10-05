import dados


def play():
    """Coleta a opção de jogada que por ser 'X' ou 'O' e a posição de inserção no tabuleiro."""
    op_user = str(input("\n\n\n\nEscolha uma pedra['X' ou 'O']: "))
    op_user = op_user.upper()

    position = int(input("Qual posição: "))

    return op_user, position


def update_positions(opt, position):
    """Atualiza as posições no tabuleiro."""
    dados.posicoes[position] = opt
    return
