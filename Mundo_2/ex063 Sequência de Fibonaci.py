#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('=' * 30)
print('Sequência de Fibonacci')
print('=' * 30)

termos = int(input('Quantos termos você quer mostrar? '))
print('~~~' * 20)
cont = 0
termo1 = 0
termo2 = 1

#Esse while serve para mostrar os termos
while cont < termos:
    cont +=1
    #As duas primeiras condições são simples. Mostram os 2 primeiros termos
    if cont == 1:
        print(termo1, end=' -> ')
    elif cont == 2:
        print(termo2, end=' -> ')
    #Esse else verifica se já passamos dos dois primeiros termos, e em caso positivo, ele começa a fazer a soma e a
    #reatribuir as variáveis
    else:
        termo3 = termo1 + termo2
        print(termo3, end=' -> ')
        termo1 = termo2
        termo2 = termo3
print('FIM')

