#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual é o seu nome completo? ')).strip()

# Verificamos se 'SILVA' existe dentro do nome convertido para maiúsculas
tem_silva = 'SILVA' in nome.upper()

print(f'Seu nome tem Silva? {tem_silva}')