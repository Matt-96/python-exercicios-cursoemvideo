#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O
# programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão: '))
tot_termo = 0

termo = primeiro
termos = 10
while termos != 0:
    contador = 0
    while contador < termos:
        print(f'{termo} -> ', end='')
        contador += 1
        termo += razao
        tot_termo +=1

    print('PAUSA')
    termos = int(input('Quantos termos mais você quer mostrar? (DIGITE 0 PARA ENCERRAR.)'))
print(f'A progressão foi finalizada com {tot_termo} termos mostrados.')
