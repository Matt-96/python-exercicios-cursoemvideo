from colorama import init, Fore
init(autoreset=True)
def linha():
    print('-' * 50)
def cabecalho(msg):
    linha()
    print(f'{msg:^50}')
    linha()


def menu():
    cabecalho('MENU PRINCIPAL')

    print(Fore.YELLOW + '1','-', Fore.BLUE + 'Ver Pessoas Cadastradas')
    print(Fore.YELLOW + '2', '-', Fore.BLUE + 'Cadastrar Nova Pessoa')
    print(Fore.YELLOW + '3', '-', Fore.BLUE + 'Sair do Sistema')
    linha()