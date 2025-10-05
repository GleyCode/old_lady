# --- Módulos externos
import sys

# --- Módulos internos
import cli
import regras
import dados


def main():
    """Executa o jogo. 
    Primeiro é obtido os valores de 'pedra' e posição no tabuleiro. 
    Em seguida, o tabuleiro é atualizado; 
    depois com os valores do tabuleito atualizamos o CLI.
    Por fim, é verificado os arranjos possíveis de vitória.
    """
    cli.mostrar_titulo()
    cli.mostrar_tabuleiro()
    
    while True:
        try:
            opt = str(input("\n\n\n\nEscolha uma pedra['X' ou 'O']: ")).upper()
            posicao = int(input("Qual posição: "))
        except (ValueError):
            print("Pedra inválida! Tente novamente.")
            continue
        except KeyboardInterrupt:
            sys.exit()
        else:
            cli.limpar_tela()
            cli.mostrar_titulo()

            # Verifica se a opção do usuário é uma opção permitida.
            if opt in dados.opts:
                dados.atualizar_posicao(opt, posicao)
                cli.mostrar_tabuleiro()
                E_vitoria = regras.verificar_vitoria()

                # Confirma a vitória
                if E_vitoria == True:
                    cli.mostrar_mensagem_vitoria()
                    break
                continue
            else:
                print("Pedra inválida! Tente novamente.")
                continue


# execução do jogo
if __name__ == "__main__":
    main()
