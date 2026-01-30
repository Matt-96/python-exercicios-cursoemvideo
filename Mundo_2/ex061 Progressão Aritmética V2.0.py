#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão: '))

contador = 0
termo = primeiro


while contador < 10:
    print(f'{termo} -> ', end='')
    contador += 1
    termo += razao
print('FIM')