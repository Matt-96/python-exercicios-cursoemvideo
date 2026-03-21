from colorama import init, Fore
from Mundo_3.ex113.funções_matematicas import *
init(autoreset=True)
def linha():
    print('-' * 50)
def cabecalho(msg):
    linha()
    print(f'{msg:^50}')
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(Fore.YELLOW + f'{c}', '-',Fore.BLUE + f'{item}')
        c+=1
    linha()
    opc = leiaInt(Fore.GREEN + 'Sua opção:')
    return opc





