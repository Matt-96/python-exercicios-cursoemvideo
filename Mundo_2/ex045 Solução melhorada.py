#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from random import  randint

itens = ('PEDRA', 'PAPEL' ,'TESOURA')
comp = random.randint(0,2)
jogador = int(input("""
Suas opções::
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
"""))
if jogador > 2:
    print('OPÇÃO INVALIDA! PROGRAMA ENCERRADO.')
else:
    #Essa condição testa qualquer empate. Reduzindo algumas linhas no volume do código
    # Em vez de comparar o texto, compare o número da jogada:
    if jogador == comp:
        print('EMPATE!')
    #Essa linha testa todas as possibilidades de vitória do jogador
    elif (jogador == 0 and comp == 2) or (jogador == 1 and comp == 0) or (jogador == 2 and comp == 1):
        print(f'Você escolheu {itens[jogador]} e eu {itens[comp]}. VOCÊ VENCEU!')
    #Essa aqui testa as derrotas
    else:
        print(f'Eu escolhi {itens[comp]} e você {itens[comp]}. EU VENCI!')