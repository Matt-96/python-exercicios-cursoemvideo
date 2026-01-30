#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.5

resp = 'S'
soma = cont  =  0

while  resp == 'N':
    num = int(input('Digite um número: '))
    soma += num
    resp = str(input('Deseja continuar? [S ou N ]')).strip().upper()[0]
    #Caso o usuário insista em digitar errado
    while resp not in 'SsNn':
        print('Resposta incorreta')
        resp = str(input('Deseja continuar? [S ou N ]')).strip().upper()[0]
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

media = soma / cont


print(f'O maior número foi {maior} e o menor foi {menor}')
print(f'A soma dos valores é igual a: {media:.2f}')