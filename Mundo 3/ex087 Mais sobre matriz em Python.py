#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
somaPar = somaColuna3 = 0
matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(0, len(matriz)):
    for c in range(0, len(matriz)):
        num = int(input(f'Digite um valor para [{l}, {c}]:'))
        if num % 2 == 0:
            somaPar += num
        matriz[l][c] = num

for l in range(0, len(matriz)):
    print(end='\n')
    for c in range(0, len(matriz)):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if c == 2:
            somaColuna3 += matriz[l][c]

print(end='\n')
print('-=' * 100)
print(f'A soma dos números pares é igual a {somaPar}')
print(f'A soma dos números presentes na coluna 3 é igual a {somaColuna3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

