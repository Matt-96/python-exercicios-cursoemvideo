#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
def sorteia(lst):
    print('Sorteando 5 valores da lista:', end='')
    for c in range(1,6):
        lst.append(randint(1,10 ))
    for n in lst:
        print(n, end=' ')
        sleep(0.5)
    print('PRONTO!')


def soma_par(lst):
    print(f'Somando s valores pares de {lst} ', end='')
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'temos {soma}.')


#Programa principal
numeros = list()
sorteia(numeros)
soma_par(numeros)
