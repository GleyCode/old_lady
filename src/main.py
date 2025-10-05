import cli
import regras
import dados


def main():
    """Executa o jogo. Primeiro é obtido os valores de 'pedra' e posição no tabuleiro. Em seguida, o tabuleiro é atualizado; depois com os valores do tabuleito atualizamos o CLI, por fim, é verificado os arranjos possíveis de vitória.
    """
    cli.mostrar_titulo()
    cli.mostrar_tabuleiro()
    
    while(True):
        try:
            opt = str(input("\n\n\n\nEscolha uma pedra['X' ou 'O']: ")).upper()
            posicao = int(input("Qual posição: "))
        except:
            pass
        else:
            cli.limpar_tela()
            cli.mostrar_titulo()

            if opt in dados.opts:
                dados.atualizar_posicao(opt, posicao)
                cli.mostrar_tabuleiro()
                status = regras.verificar_vitoria()

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
