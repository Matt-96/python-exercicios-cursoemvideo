#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
ano_atual = datetime.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    pessoa = int (input(f'Em que ano a {pess}° pessoa nasceu ?'))
    idade = ano_atual - pessoa
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Tivemos {maior} maiores de idade.')
print(f'Tivemos {menor} menores de idade.')
