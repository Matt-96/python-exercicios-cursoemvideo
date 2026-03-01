#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa
#tem que realizar três contagens através da função criada.
#A) de 1 até 10, de 1 em 1
#B) de 10 até 0, de 2 em 2
#C) uma contagem personalizada
from time import sleep
def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if f <= 0:
        for c in range(i, f-1, -p):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
        print('-=' * 20)
    else:
        for c in range(i, f + 1, p):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5-1)
        print('FIM!')
        print('-=' * 20)


#Programa principal
contador(1,10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Inicio:'))
Fim = int(input('Fim:'))
Passo = int(input('Passo: '))
if Passo < 0:
    Passo = Passo - (Passo* 2)
elif Passo == 0:
    Passo = 1
contador(inicio,Fim, Passo)
