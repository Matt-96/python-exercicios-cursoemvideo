#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print(f'O dobro de {n} vale {dobro}.')
print(f'O triplo de {n} vale {triplo}.')
print(f'A raiz quadrada de {n} é igual a {raiz:.2f}.')