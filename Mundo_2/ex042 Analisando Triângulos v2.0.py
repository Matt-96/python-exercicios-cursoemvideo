#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

print('-=' * 20)
print('ANALISADOR DE TRIÂNGULOS V2.0')
print('-=' * 20)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

#Condição de existência de um Triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um Triângulo!')
    #Condição Triângulo Equilátero
    if r1 == r2 == r3:
        print('Os segmentos acima formam um Triângulo Equilátero.')
    #Condição Triângulo Isósceles
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Os segmentos acima formam um Triângulo Isosceles.')
    #Condição Triângulo Escaleno
    elif r1 != r2 != r3:
        print('Os segmentos acima formam um Triângulo Escaleno.')
else:
    print('Os segmentos acima NÃO podem formar um Triângulo.')