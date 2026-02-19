#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
numeros = []
while True:
    resp = ' '
    n = int(input('Digite um número: '))
    numeros.append(n)

    while resp not in 'SN':
        resp = input('Deseja continuar? [S / N]').strip().upper()[0]
    if resp == 'N':
        break

print(f'Você digitou {len(numeros)} elementos.')
print(f'Os valores em ordem decrescente são: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista.')
