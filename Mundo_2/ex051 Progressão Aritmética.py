#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('=' * 40)
print('10 termos de uma PA')
print('=' * 40)

primeiro = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))
decimo = primeiro + (10 - 1) * razao

for n in range(primeiro, decimo + razao, razao):
    print(n, end=' -> ')
print('ACABOU')