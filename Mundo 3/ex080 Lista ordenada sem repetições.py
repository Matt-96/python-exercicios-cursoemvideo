#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Adicionado ao final da lista.')
    else:
        for cont in range(0, len(numeros)):
            if num <= numeros[cont]:
                numeros.insert(cont, num)
                print(f'Adicionado na posição {cont}')
                break



print(numeros)