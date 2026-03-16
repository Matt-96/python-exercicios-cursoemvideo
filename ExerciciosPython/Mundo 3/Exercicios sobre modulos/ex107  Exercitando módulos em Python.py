#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
# e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
from utilidadesCeV import moeda


preco = float(input('Digite o preço: R$'))

print(f'A metade de R${preco} é R${moeda.metade(preco):.2f}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco):.2f}')
print(f'Aumentando 10% temos R${moeda.aumentar(preco, 10):.2f}')
print(f'Diminuindo 10% temos R${moeda.diminuir(preco,10):.2f}')