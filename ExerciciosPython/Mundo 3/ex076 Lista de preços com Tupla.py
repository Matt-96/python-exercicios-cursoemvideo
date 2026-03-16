#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.50, 'Borracha',1.00, 'Caneta', 1.50, 'Caderno', 5.00 )
print(f'-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(f'-' * 40)
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p] :.<30}', end='')
    else:
        print(f'R${produtos[p]:>7.2f}')
print('-' * 40)