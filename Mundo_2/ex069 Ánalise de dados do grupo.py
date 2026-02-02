#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

print('-' * 30)
print('CADASTRE UMA PESSOA')
print('-' * 30)
mais_18 = mulher_20menos = homens = 0

while True:
    resp =' '
    sexo = ' '
    idade = int(input('Idade: '))
    #Checa se é maior de idade
    if idade > 18:
        mais_18 += 1
    #Valida se o usuário digitou o sexo corretamente
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M / F]')).strip().upper()
    #Checa se a pessoa cadastrada é homem, em caso positivo soma-se mais um na variável homens
    if sexo == 'M':
        homens += 1
    #Checa se é uma mulher com menos de 20 anos.
    elif sexo == 'F' and idade < 20:
        mulher_20menos += 1
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S / N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mais_18} pessoas maiores de 18 anos.')
print(f'Foram cadastradas {mulher_20menos} mulheres com menos de 20 anos.')