#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número para calcular seu fatorial: '))
fat = num
resultado = 1
print(f'Calculando {num}!')
while fat > 0:
    #Para exibir o cálculo de fatorial
    print(f'{fat}', end=' X ') if fat > 1 else print(f'{fat} = ' , end='')
    #Para fazer a operação de fatorial
    resultado *= fat
    fat -= 1

print(f'{resultado}')