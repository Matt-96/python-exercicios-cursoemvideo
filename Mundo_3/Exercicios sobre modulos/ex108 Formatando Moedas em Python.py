#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar
# os números como um valor monetário formatado.

from utilidadesCeV import moeda


preco = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(preco)} é R${moeda.metade(preco)})')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco)}')
print(f'Aumentando 10% temos {moeda.aumentar(preco, 10)}')
