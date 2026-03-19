from funções_matematicas import leiaInt, leiaFloat
n = leiaInt('Digite um número: ')
if n is None:
    print('O usuário não informou nenhum valor.')
else:
    print(f'Você digitou o número {n}')

n = leiaFloat('Digite um número: ')

if n is None:
    print('O usuário não informou nenhum valor.')
else:
    print(f'Você digitou o número {n}')
