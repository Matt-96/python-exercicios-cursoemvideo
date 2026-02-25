#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
#visualização de detalhes do aproveitamento de cada jogador.
time = list ()
jogador = dict()
while True:
    jogador['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Gols'] = list()
    jogador['Total'] = 0
    resp = ' '
    if partidas > 0:
        for c in range(0, partidas):
            qtdGol = int(input(f'Quantos gols na partida {c+1}? '))
            jogador['Total']+=qtdGol
            jogador['Gols'].append(qtdGol)
    time.append(jogador.copy())
    jogador.clear()
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(time)
print('-=' *30)
print(f'{"No.":<4}{"Nome":<15}{"Gols":<15}{"Total":<5}')

for cont, j  in enumerate(time):
    print(f'{cont:<4}{j["Nome"]:<15}{str(j["Gols"]):<15}  {j["Total"]:<5}')
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    if  opc >= len(time) or opc < 0:
        print('Opção inválida tente novamente.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[opc]['Nome']}:')
        for c in range(0, len(time[opc]['Gols'])):
            print(f'No jogo {c+1} ele marcou {time[opc]["Gols"][c]}')