import os
import time
from dados import posicoes


def limpar_tela():
    """Limpa a prompt de acordo com a paltaforma especifica."""
    if os.name == 'nt':
        os.system('cls')
    os.system('clear')


def pausar_fluxo():
    """Para a execução do jogo por 1,5 segundos."""
    time.sleep(1.5)


def mostrar_titulo():
    """Título princípal do jogo. É chamado somente no início."""        
    print("-" * 120)
    print("OLD LADY".center(120))
    print("\nVersão 1.2")
    print("Desenvolvido por Abraão A. Silva\n")
    print("-" * 120)
        

def mostrar_tabuleiro():
    """CLI atualizado em tempo de execução por um dicionário."""    
    tabuleiro = f"""
        {posicoes[1]:<3} | {posicoes[2]:<3} | {posicoes[3]:<3}
        ---------------
        {posicoes[4]:<3} | {posicoes[5]:<3} | {posicoes[6]:<3}
        ---------------
        {posicoes[7]:<3} | {posicoes[8]:<3} | {posicoes[9]:<3}
        """
    print(tabuleiro)


def mostrar_mensagem_vitoria():
    """Mostra uma mensagem de vitória animada."""
    mensagem = "VITÓRIA!!! PARABÉNS .)"
    for i in range(3):
        match i:
            case 0:
                print(f"\n{"-" * 120}")
                print("\n" + mensagem.center(40))
                print(f"\n{"-" * 120}")
            case 1:
                print(f"\n{"-" * 120}")
                print("\n" + mensagem.center(80))
                print(f"\n{"-" * 120}")
            case 2:
                print(f"\n{"-" * 120}")
                print("\n" + mensagem.center(40))
                print(f"\n{"-" * 120}")
        pausar_fluxo()
        limpar_tela()
