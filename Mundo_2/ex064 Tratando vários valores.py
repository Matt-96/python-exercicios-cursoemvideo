#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
#usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
# soma entre eles (desconsiderando o flag).
numero = tot_num = soma = 0
while numero != 999:
    numero = int(input('Digite um número. [Digite 999 para parar]: '))
    if numero > 999 or numero < 999:
        tot_num += 1
        soma += numero
print(f'Foram digitados {tot_num} números e a soma entre eles é {soma}')
