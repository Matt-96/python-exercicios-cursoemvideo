#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from utilidadesCeV import moeda


preco = float(input('Digite o preço: R$'))

print(f'A metade de {moeda(preco)} é R${moeda.metade(preco,False)}')
print(f'O dobro de {moeda(preco)} é {moeda.dobro(preco,False)}')
print(f'Aumentando 10% temos {moeda.aumentar(preco, 10, False)}')
