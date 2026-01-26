#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
from colorama import Fore

dividido = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        dividido += 1
        print(Fore.YELLOW +str (c), end=' ')
    else:
        print(Fore.RED + str(c), end=' ')
if dividido == 2:

    print(Fore.BLUE + f'\nO número {n} foi dividido {dividido} vezes. Por 1 e por ele mesmo por isso é primo.')
elif dividido > 2:
    print(Fore.BLUE + f'\nO número {n} foi dividido {dividido} vezes, e por isso ele não é primo')
