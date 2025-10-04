from os import system


window_messege = ""


def title():
        """Título princípal do jogo. É chamado somente no início."""
        window_messege = "{}\n\t\t\t\t\t\t\tJOGO DA VELHA\n{}\nversão 1.0\nBy Abraão Alves da Silva\n{}\n\n\n\n".format('-'*120, '-'*120, '*'*120)
        print(window_messege)
        

def window_tabuleiro(positions:dict):
        """Interface de linha de comando atualizada em tempo de execução por um dicionário."""
        window_messege = """\t.\t.\n\t.\t.\n   {}\t.   {}\t.   {}\n. . . . . . . . . . . . .\n\t.\t.\n   {}\t.   {}\t.   {}\n\t.\t.\n. . . . . . . . . . . . .\n\t.\t.\n   {}\t.   {}\t.   {}\n\t.\t.
        """.format(positions[1], positions[2], positions[3], positions[4], positions[5], positions[6], positions[7], positions[8], positions[9]) 
        print(window_messege)


def window_wins():
        """Mensagem de vitória."""
        window_messege = "VITÓRIA!!! PARABÉNS .)"
        print("\n{}".format('+'*120))
        print("\n" + window_messege)
        print("\n{}".format('*'*120))


def window_clear():
        system("clear")
