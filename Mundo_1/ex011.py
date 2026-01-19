#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Largura da parede (m): '))
alt = float(input('Altura da parede (m): '))

area = larg * alt
tinta = area / 2

print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area:.3f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.4f}l de tinta.')