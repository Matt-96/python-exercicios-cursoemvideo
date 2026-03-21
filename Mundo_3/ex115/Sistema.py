from interface import menu, cabecalho
from time import sleep
from colorama import init, Fore
init(autoreset=True)

while True:
    sleep(2)
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('OPÇÃO 1')
    elif resposta == 2:
        cabecalho('OPÇÃO 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema ... Até logo!')
        break
    else:
        print(Fore.RED +  'Digite uma opção válida!')



