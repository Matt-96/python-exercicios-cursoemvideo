#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
valores = 0
for c in range(1, 501, 2):
    #O for faz a contagem, e essa condição verifica se é um número multiplo de 3 e se é ímpar
    if c % 3 == 0:
        soma +=  c
        valores +=1
print(f'A soma de todos os {valores} valores solicitados é {soma}')
