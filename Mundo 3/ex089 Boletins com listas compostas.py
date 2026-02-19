#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.
alunos = []
dados = []

while True:
    resp = ' '
    nome = input('Nome:')
    dados.append(nome)
    nota1 = float(input('Nota 1:'))
    dados.append(nota1)
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    dados.append(nota2)
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    while resp not in 'SN':
        resp = input('Deseja continuar? [S / N] ').strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{'No.':<4}', f'{'NOME':<10}', f'{'MEDIA':>8}' )
for cont, a in enumerate(alunos):

    print(f'{cont:<4}',f'{a[0]:<10}', f'{alunos[cont][3]:>7}')
print('-' * 50)
while True:

    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))

    if opc == 999:
        break
    print(f'Notas de {alunos[opc][0]} são {alunos[opc][1:3]}')