#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
pessoas = []
dados = []
maisPesados = []
maisLeves = []
while True:
    resp = ' '
    nome = input('Nome:')
    dados.append(nome)

    peso = int(input('Peso: '))
    dados.append(peso)
    #cria uma cópia dos dados e joga dentro da lista pessoas
    pessoas.append(dados[:])
    #limpa os dados para receber o cadastro de uma nova pessoa.
    dados.clear()
    while resp not in 'SN':
        resp = input('Deseja continuar? [S / N]').strip().upper()
    if resp == 'N':
        break
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
for p in range(0, len(pessoas)):
    if p == 0:
        maisPesados.append(pessoas[p])
        maisLeves.append(pessoas[p])

    else:
        if maisPesados[0][1] == pessoas[p][1]:
            maisPesados.append(pessoas[p])
        elif maisPesados[0][1] < pessoas[p][1]:
            maisPesados.clear()
            maisPesados.append(pessoas[p])
        if maisLeves[0][1] == pessoas[p][1]:
            maisLeves.append(pessoas[p])
        elif maisLeves[0][1] > pessoas[p][1]:
            maisLeves.clear()
            maisLeves.append(pessoas[p])


print(f'O maior peso foi de {maisPesados[0][1]}.Peso de:', end='')
for p in maisPesados:
    print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {maisLeves[0][1]}.Peso de', end='')
for p in maisLeves:
    print(f'[{p[0]}]', end=' ')

