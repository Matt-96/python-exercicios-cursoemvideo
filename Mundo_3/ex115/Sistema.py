from interface import menu, cabecalho
from Mundo_3.ex113.funções_matematicas import leiaInt
from colorama import init, Fore
from time import sleep

init(autoreset=True)
while True:
    sleep(1)
    menu()
    opc = leiaInt(Fore.GREEN + 'Sua Opção:')
    if opc == 1:
        cabecalho('OPÇÃO 1')
    elif opc == 2:
        cabecalho('OPÇÃO 2')
    elif opc == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print(Fore.RED + 'Digite uma opção válida.')