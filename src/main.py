import entry
import cli
import rules
import dados


def main():
    """Executa o jogo. Primeiro é obtido os valores de 'pedra' e posição no tabuleiro. Em seguida, o tabuleiro é atualizado; depois com os valores do tabuleito atualizamos o CLI, por fim, é verificado os arranjos possíveis de vitória.
    """
    cli.mostrar_titulo()
    cli.mostrar_tabuleiro()
    
    while(True):
        opt, position = entry.play()
        cli.limpar_tela()
        cli.mostrar_titulo()

        if opt in dados.opts:
            entry.update_positions(opt, position)
            cli.mostrar_tabuleiro()
            status = rules.verificar_vitoria()

            if status == 1:
                cli.mostrar_mensagem_vitoria()
                break
            continue
        else:
            print("Pedra inválida! Tente novamente.")
            continue


# execução do jogo
if __name__ == "__main__":
    main()
