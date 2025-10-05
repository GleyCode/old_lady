# posições do tabuleiro e seus valores atribuidos
posicoes = {1: '[1]', 2: '[2]', 3: '[3]', 
            4: '[4]', 5: '[5]', 6: '[6]', 
            7: '[7]', 8: '[8]', 9: '[9]'}

# entradas possíveis
opts = ('X', 'O')


def atualizar_posicao(opt, position):
    """Atualiza as posições no tabuleiro."""
    posicoes[position] = opt
