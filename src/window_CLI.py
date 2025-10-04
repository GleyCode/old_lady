import os


def limpar_tela():
        """Limpa a prompt de acordo com a paltaforma especifica."""
        if os.name == 'nt':
                os.system('cls')
        os.system('clear')


def mostrar_titulo():
        """Título princípal do jogo. É chamado somente no início."""        
        print("-" * 120)
        print("OLD LADY".center(120))
        print("\nVersão 1.2")
        print("Desenvolvido por Abraão A. Silva\n")
        print("-" * 120)
        

def mostrar_tabuleiro(positions: dict):
        """CLI atualizado em tempo de execução por um dicionário."""
        global mensagem_tela
        mensagem_tela = """\t.\t.\n\t.\t.\n   {}\t.   {}\t.   {}\n. . . . . . . . . . . . .\n\t.\t.\n   {}\t.   {}\t.   {}\n\t.\t.\n. . . . . . . . . . . . .\n\t.\t.\n   {}\t.   {}\t.   {}\n\t.\t.
        """.format(positions[1], positions[2], positions[3], positions[4], positions[5], positions[6], positions[7], positions[8], positions[9]) 
        return mensagem_tela


def mostrar_mensagem_vitoria():
        """Mensagem de vitória."""
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
