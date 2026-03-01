#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
#retangular(largura e comprimento) e mostre a área do terreno.
def area(l, c):
    produto = l*c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {produto:.1f}m²')


#Programa Principal
print('   Controle de Terrenos')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)