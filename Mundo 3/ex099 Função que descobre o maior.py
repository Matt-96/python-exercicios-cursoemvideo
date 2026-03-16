#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    cont = 0
    maior_num = 0
    for n in num:
        if cont == 0:
            maior_num = n
        else:
            if n > maior_num:
                maior_num = n
        print(n, end=' ')
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior_num}.')



#Programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()