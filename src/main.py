import entry
import window_CLI
import rules
import struct_data


def main():
    """Executa o jogo. Primeiro é obtido os valores de 'pedra' e posição no tabuleiro. Em seguida, o tabuleiro é atualizado; depois com os valores do tabuleito atualizamos o CLI, por fim, é verificado os arranjos possíveis de vitória.
    """
    window_CLI.title()
    # tabuleiro inicial
    window_CLI.window_tabuleiro(struct_data.positions)
    
    while(True):
        opt, position = entry.play()
        window_CLI.window_clear()
        window_CLI.title()

        if (opt in struct_data.opts):
            entry.update_positions(opt, position)
            window_CLI.window_tabuleiro(struct_data.positions)
            status = rules.verify_wins()

            if status == 1:
                window_CLI.window_wins()
                break

            continue
        else:
            print("Pedra inválida! Tente novamente.")
            continue


# execução do jogo
if __name__ == "__main__":
    main()
