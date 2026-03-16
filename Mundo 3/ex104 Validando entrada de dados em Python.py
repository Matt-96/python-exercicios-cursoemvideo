#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função
# input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

def LeiaInt(msg):
    from colorama import Fore,  init
    init(autoreset=True)
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print(Fore.RED + 'ERRO! Digite um número inteiro válido.')


#Programa principal
n = LeiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}.')