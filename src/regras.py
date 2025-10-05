import dados


def verificar_vitoria():
    """No jogo da velha são possíveis oito arranjos. Esse função testa para uma de duas posibilidades em cada arranjo.Em cada arranjo podemos ter a vitória de 'O' ou 'X'.
    """

    # arranjo (1-5-9)
    if dados.posicoes[1] == "X" and dados.posicoes[5] == "X" and dados.posicoes[9] == "X":
        return True
    if dados.posicoes[1] == "O" and dados.posicoes[5] == "O" and dados.posicoes[9] == "O":
        return True

    # arranjo (2-5-8)
    if dados.posicoes[2] == "X" and dados.posicoes[5] == "X" and dados.posicoes[8] == "X":
        return True
    if dados.posicoes[2] == "O" and dados.posicoes[5] == "O" and dados.posicoes[8] == "O":
        return True

    # arranjo (1-2-3)
    if dados.posicoes[1] == "X" and dados.posicoes[2] == "X" and dados.posicoes[3] == "X":
        return True
    if dados.posicoes[1] == "O" and dados.posicoes[2] == "O" and dados.posicoes[3] == "O":
        return True

    # arranjo (7-5-3)
    if dados.posicoes[7] == "X" and dados.posicoes[5] == "X" and dados.posicoes[3] == "X":
        return True
    if dados.posicoes[7] == "O" and dados.posicoes[5] == "O" and dados.posicoes[3] == "O":
        return True

    # arranjo (3-6-9)
    if dados.posicoes[3] == "X" and dados.posicoes[6] == "X" and dados.posicoes[9] == "X":
        return True
    if dados.posicoes[3] == "O" and dados.posicoes[6] == "O" and dados.posicoes[9] == "O":
        return True

    # arranjo (1-4-7)
    if dados.posicoes[1] == "X" and dados.posicoes[4] == "X" and dados.posicoes[7] == "X":
        return True
    if dados.posicoes[1] == "O" and dados.posicoes[4] == "O" and dados.posicoes[7] == "O":
        return True

    # arranjo (4-5-6)
    if dados.posicoes[4] == "X" and dados.posicoes[5] == "X" and dados.posicoes[6] == "X":
        return True
    if dados.posicoes[4] == "O" and dados.posicoes[5] == "O" and dados.posicoes[6] == "O":
        return True

    # arranjo (7-8-9)
    if dados.posicoes[7] == "X" and dados.posicoes[8] == "X" and dados.posicoes[9] == "X":
        return True
    if dados.posicoes[7] == "O" and dados.posicoes[8] == "O" and dados.posicoes[9] == "O":
        return True
