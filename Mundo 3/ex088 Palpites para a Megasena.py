#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import  randint
from time import sleep
jogos = []
jogo = []

print('-' * 40)
print(f'{'JOGA NA MEGASENA':^40}')
print('-' * 40)
qtdDejogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 5, f'SORTEANDO {qtdDejogos} JOGOS', '=' * 5)
for c in range(0, qtdDejogos):
    cont = 0
    while cont < 6:

        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            cont += 1
    jogos.append(jogo[:])
    jogo.clear()
    print(f'Jogo{c + 1}: {sorted(jogos[c])}')
    sleep(0.5)
print('-=' * 5, '< BOA SORTE! >', '=-' * 5)

