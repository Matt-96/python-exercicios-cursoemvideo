# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
menos_20 = 0
mais_velho_nome = ''
mais_velho_idade = 0
for c in range(1, 5):
    nome = input(f'Digite o nome da {c}° pessoa: ')
    idade = int(input(f'Digite a idade da {c}º pessoa: '))
    soma_idade += idade
    sexo = input(f'Digite o sexo da {c}º pessoa:  (M / F) ').upper().strip()
    ##Essa condição verifica se é homem e se é o mais velho
    if sexo == 'M' and idade > mais_velho_idade:
        mais_velho_nome = nome
        mais_velho_idade = idade

    else:
        # Mulher com menos de 20 anos
        if idade < 20 and sexo == 'F':
            menos_20 += 1
print(f'O homem mais velho se chama {mais_velho_nome} e ele tem {mais_velho_idade} anos.')
print(f'A média de idade do grupo é {soma_idade / 4:.1f}')
print(f'No total temos {menos_20} mulheres com menos de 20 anos no grupo.')