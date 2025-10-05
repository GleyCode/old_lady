# posições do tabuleiro e seus valores atribuidos
posicoes = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

# entradas possíveis
opts = ('X', 'O')


def atualizar_posicao(opt, position):
    """Atualiza as posições no tabuleiro."""
    posicoes[position] = opt
