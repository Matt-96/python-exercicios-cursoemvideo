#xercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

# Exercício Python 022: Analisador de Textos
# Objetivo: Manipular strings para extrair informações específicas.

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

# Para contar sem espaços: pegamos o tamanho total e subtraímos a contagem de espaços
letras_totais = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {letras_totais} letras')

# Para o primeiro nome: podemos fatiar a string até o primeiro espaço encontrado
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras')