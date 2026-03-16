#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(0, len(matriz)):
    for c in range(0, len(matriz)):
        num = int(input(f'Digite um valor para [{l}, {c}]:'))
        matriz[l][c] = num

for l in range(0, len(matriz)):
    print(end='\n')
    for c in range(0, len(matriz)):
        print(f'[{matriz[l][c]:^5}]', end=' ')