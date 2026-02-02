#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
texto = 'BANCO CEV'
print('=' * 40)
print(f'{texto:^40}')
print('=' * 40)
nota = 50
ced = 50
cedTot = 0
valor = int(input('Qual valor você quer sacar? R$'))
total = valor

while True:
    if ced <= total:
        total -= ced
        cedTot += 1

    else:
        if cedTot > 0:
            print(f'Total de notas de R${ced}:{cedTot}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cedTot = 0

        if total == 0:
            break

