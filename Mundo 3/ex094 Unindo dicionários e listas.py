#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

pessoa = dict ()
pessoas = list ()
mulheres = list()
somaIdade = 0
while True:
    resp = ' '
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M / F]')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M / F]')).strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('Deseja continuar? [S / N]')).strip().upper()[0]
    while resp not in 'SN':
        print(f'ERRO! Digite apenas S ou N.')
        resp = str(input('Deseja continuar? [S / N]')).strip().upper()[0]

    if resp == 'N':
        break
media = somaIdade / len(pessoas)
print(pessoas)
print(f'A) Ao todo foram cadastradas {len(pessoas)}')
print(f'B) A média de idade é de {media:.2f}')
if len(mulheres)> 0:
    print(f'C) As mulheres cadastradas foram:', end=' ')
    for n in mulheres:
        print(f'[{n}]', end=' ')
    print()
print(f'D) Lista de pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > media:
        print(f'Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]}')
