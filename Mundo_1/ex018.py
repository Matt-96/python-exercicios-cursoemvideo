#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.

import math

angulo = float(input('Digite o ângulo que você deseja: '))

# Convertendo para radianos antes de calcular
radiano = math.radians(angulo)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'O ângulo de {angulo}° tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo}° tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo}° tem a TANGENTE de {tangente:.2f}')