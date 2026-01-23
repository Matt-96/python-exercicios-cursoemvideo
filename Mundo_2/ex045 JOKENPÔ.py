#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
comp = randint(1, 3)
jogador = int(input('Suas opções: \n'
                    '[ 1 ] PEDRA'
                    '[ 2 ] PAPEL'
                    '[ 3 ] TESOURA\n'
                    'Qual é a sua jogada?'))

if jogador < 1 or jogador > 3:
    print('OPÇÃO INVÁLIDA! JOGO ENCERRADO!')
else:
    print('JO...')
    sleep(0.3)
    print('KEN...')
    sleep(0.3)
    print('PÔ!')

    if jogador == 1 and comp == 1:
        print('Nós dois jogamos pedra. EMPATE!')
    elif jogador == 1 and comp == 2:
        print('Você jogou pedra e eu papel. VENCI!')
    elif jogador == 1 and comp == 3:
        print('Você jogou pedra e eu tesoura. VOCÊ VENCEU!')
    elif jogador == 2 == comp:
        print('Nós dois jogamos papel. EMPATE!')
    elif jogador == 2 and comp == 1:
        print('Você jogou papel e eu pedra. VOCÊ VENCEU!')
    elif jogador == 2 and comp == 3:
        print('Você jogou papel e eu tesoura. VENCI!')
    elif jogador == 3 == comp:
        print('Nós dois jogamos tesoura. EMPATE!')
    elif jogador == 3 and comp == 1:
        print('Você jogou tesoura e eu pedra. VENCI!')
    else:
        print('Você jogou tesoura e eu papel. VOCÊ VENCEU!')

