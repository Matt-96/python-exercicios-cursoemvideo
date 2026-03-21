#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
#extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
#mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []
while True:
    resp = ' '
    n = int(input('Digite um número: '))
    numeros.append(n)
    while resp not in 'SN':
        resp = input('Deseja continuar? [S / N]').strip().upper()[0]
    if resp == 'N':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Os números cadastrados foram: {numeros}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números ímpares é: {impares}')