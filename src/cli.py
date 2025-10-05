# --- Módulos externo
import os
import time

# --- Módulos interno
from dados import posicoes


def limpar_tela():
    """Limpa a prompt de acordo com a paltaforma especifica."""
    if os.name == 'nt':
        os.system('cls')
    os.system('clear')


def pausar_tela():
    """Para a execução do jogo por 1,5 segundos."""
    time.sleep(1.5)


def mostrar_titulo():
    """Título princípal do jogo. É chamado somente no início."""        
    print("-" * 120)
    print("OLD LADY".center(120))
    print("\nVersão 1.2")
    print("Desenvolvido por Abraão A. Silva\n")
    print("-" * 120)
    print("\n")
        

def mostrar_tabuleiro():
    """Atualiza o CLI em tempo de execução com um dicionário."""    
    print(f"{"":<4} : {"":<4} : {"":<4}".center(120))
    print(f"  {posicoes[1]:^4}:  {posicoes[2]:^4}: {posicoes[3]:^4}".center(120))
    print("..................".center(120))
    print(f"{"":<4} : {"":<4} : {"":<4}".center(120))
    print(f"  {posicoes[4]:^4}: {posicoes[5]:^4} : {posicoes[6]:^4}".center(120))
    print("..................".center(120))
    print(f"  {posicoes[7]:^4}: {posicoes[8]:<4} : {posicoes[9]:<4}".center(120))
    print(f"{"":<4} : {"":<4} : {"":<4}".center(120))


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
        pausar_tela()
        limpar_tela()
