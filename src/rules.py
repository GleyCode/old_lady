import struct_data


def verify_wins():
    """No jogo da velha são possíveis oito arranjos. Esse função testa para uma de duas posibilidades em cada arranjo.Em cada arranjo podemos ter a vitória de 'O' ou 'X'."""

    # arranjo (1-5-9)
    if struct_data.positions[1] == "X" and struct_data.positions[5] == "X" and struct_data.positions[9] == "X":
        return 1
    if struct_data.positions[1] == "O" and struct_data.positions[5] == "O" and struct_data.positions[9] == "O":
        return 1

    # arranjo (2-5-8)
    if struct_data.positions[2] == "X" and struct_data.positions[5] == "X" and struct_data.positions[8] == "X":
        return 1
    if struct_data.positions[2] == "O" and struct_data.positions[5] == "O" and struct_data.positions[8] == "O":
        return 1

    # arranjo (1-2-3)
    if struct_data.positions[1] == "X" and struct_data.positions[2] == "X" and struct_data.positions[3] == "X":
        return 1
    if struct_data.positions[1] == "O" and struct_data.positions[2] == "O" and struct_data.positions[3] == "O":
        return 1

    # arranjo (7-5-3)
    if struct_data.positions[7] == "X" and struct_data.positions[5] == "X" and struct_data.positions[3] == "X":
        return 1
    if struct_data.positions[7] == "O" and struct_data.positions[5] == "O" and struct_data.positions[3] == "O":
        return 1

    # arranjo (3-6-9)
    if struct_data.positions[3] == "X" and struct_data.positions[6] == "X" and struct_data.positions[9] == "X":
        return 1
    if struct_data.positions[3] == "O" and struct_data.positions[6] == "O" and struct_data.positions[9] == "O":
        return 1

    # arranjo (1-4-7)
    if struct_data.positions[1] == "X" and struct_data.positions[4] == "X" and struct_data.positions[7] == "X":
        return 1
    if struct_data.positions[1] == "O" and struct_data.positions[4] == "O" and struct_data.positions[7] == "O":
        return 1

    # arranjo (4-5-6)
    if struct_data.positions[4] == "X" and struct_data.positions[5] == "X" and struct_data.positions[6] == "X":
        return 1
    if struct_data.positions[4] == "O" and struct_data.positions[5] == "O" and struct_data.positions[6] == "O":
        return 1

    # arranjo (7-8-9)
    if struct_data.positions[7] == "X" and struct_data.positions[8] == "X" and struct_data.positions[9] == "X":
        return 1
    if struct_data.positions[7] == "O" and struct_data.positions[8] == "O" and struct_data.positions[9] == "O":
        return 1
