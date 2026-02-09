#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.
numeros = []
while True:
    resp = ' '
    num = int(input('Digite um valor:'))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar!')
    while resp not in 'SN':
        resp = input('Deseja continuar?').upper()[0]
    if resp == 'N':
        break
print(sorted(numeros))
