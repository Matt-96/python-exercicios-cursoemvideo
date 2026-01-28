#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

opç = 0
maior = 0
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
while opç != 5:
    opç =  int(input('''
    [ 1 ] SOMAR 
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
>>>>> Qual é a sua opção: '''))
    if opç < 1 or opç > 5:
        print('Opção inválida. Tente novamente.')
    else:
        if opç == 1:
            print(f'{num1} + {num2} = {num1 + num2}')
        elif opç == 2:
            print(f'{num1} X {num2} = {num1*num2}' )
        elif opç == 3:
            if num1 == num2:
                print('Não existe número maior')
            else:
                if num1 > num2:
                    maior = num1
                elif num1 < num2:
                    maior = num2
                print(f'O maior número é {maior}')
        elif opç == 4:
            num1 = int(input('Primeiro valor: '))
            num2 = int(input('Segundo valor: '))

