#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja
#errado, peça a digitação novamente até ter um valor correto.

sexo = input('Informe seu sexo: [M ou F]').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Por favor, digite M ou F. Tente novamente:').strip().upper()[0]
print(f'Sexo {sexo} cadastrado com sucesso.')