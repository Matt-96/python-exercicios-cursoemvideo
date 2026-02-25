#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
#visualização de detalhes do aproveitamento de cada jogador.
time = list()
jogador = dict()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    if partidas > 0:
        jogador['Gols'] = list()
        jogador['Total'] = 0
        for c in range(0, partidas):
            qtdGol = int(input(f'Quantos gols na partida {c+1}? '))
            jogador['Total']+=qtdGol
            jogador['Gols'].append(qtdGol)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite [S/N].')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'  {i:<15}', end='')
print()
print('-=' *40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('=-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para PARAR]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código{busca}.')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
        print('-=' *40)
print('<< VOLTE SEMPRE >>')
