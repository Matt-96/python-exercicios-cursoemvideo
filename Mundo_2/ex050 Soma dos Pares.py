#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
valores = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n}ºnúmero:'))
    if num % 2 == 0:
        print('Número par. Vou somar.')
        soma += num
        valores += 1
    else:
        print('Número ímpar. Não vou somar.')

print(f'A soma dos {valores} valores pares digitados é igual a {soma}.')
