#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.


numeros = []
for c in range(0,5):
    num = int(input(f'Digite um valor para a posição {c}: '))
    numeros.append(num)



print('-=' * 100)
print(f'Você digitou os valores: {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posições:',end ='')
for c in range(0, len(numeros)):
    if numeros[c] ==  max(numeros):
        print(c, end='...')
print(f'\nO menor valor digitado foi {min(numeros)} nas posições:', end='')
for c in range(0, len(numeros)):
    if numeros[c] ==  min(numeros):
        print(c,end='...')