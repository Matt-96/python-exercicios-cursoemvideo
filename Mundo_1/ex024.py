#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Em que cidade você nasceu? ')).strip()

# Verificamos se os primeiros 5 caracteres, em maiúsculo, são iguais a 'SANTO'
comeca_com_santo = cidade[:5].upper() == 'SANTO'

print(f'A cidade começa com "Santo"? {comeca_com_santo}')
