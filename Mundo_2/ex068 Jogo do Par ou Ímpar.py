#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitoria = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print(('=-' * 15))
while True:
    comp = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + comp
    escolha_jogador = ' '
    while escolha_jogador not in 'PI':
        escolha_jogador = str(input('PAR OU ÍMPAR?[P / I]')).strip().upper()[0]

    if escolha_jogador == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU')
            vitoria += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif escolha_jogador == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU!')
            vitoria += 1
        else:
            print('VOCÊ PERDEU!')
            break
print(f'GAME OVER! Você venceu {vitoria} vezes.')

