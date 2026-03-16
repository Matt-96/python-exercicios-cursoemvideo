#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
#única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[],[]]
for c in range(1,8):
    num = int(input(f'Digite o {c}º valor:  '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(f'Os números digitados foram: {numeros}')
print(f'A lista de números pares é{sorted(numeros[0])}')
print(f'A lista de números ímpares é{sorted(numeros[1])}')