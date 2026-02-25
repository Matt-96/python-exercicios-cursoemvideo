#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
#nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
#tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
jogador['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
if partidas > 0:
    jogador['Gols'] = list()
    jogador['Total'] = 0
    for c in range(0, partidas):
        qtdGol = int(input(f'Quantos gols na partida {c+1}? '))
        jogador['Total']+=qtdGol
        jogador['Gols'].append(qtdGol)
print('-=' * 30)
print(jogador)
print('-=' *30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'   ==> Na partida {c+1}, ele fez {jogador["Gols"][c]}')
print(f'Foi um total de {jogador["Total"]} gols.')