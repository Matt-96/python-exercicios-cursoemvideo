#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

#Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
aocontrario = ''

#essa linha serve para inverter a frase
for letra in range(len(junto)-1, -1, -1):
    aocontrario +=junto[letra]
if aocontrario == junto:
    print(f'O inverso de {junto} é {aocontrario}')
    print('Essa frase é um palindromo')
else:
    print(f'O inverso de {junto} é {aocontrario}')
    print('Essa frase não é um palindromo')
