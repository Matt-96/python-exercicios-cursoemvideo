#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#Uso esse módulo para pegar o ano atual do sistema
from datetime import datetime
anoAtual = datetime.today().year


anoNasc = int(input('Digite seu ano de nascimento: (Válido até o ano atual. '))
while anoNasc > anoAtual:
        print('ERRO! Digite um ano válido.')
        anoNasc = int(input('Digite seu ano de nascimento: (Válido até o ano atual. '))
else:
        idade = anoAtual - anoNasc
        print(f'Quem nasceu em {anoNasc} tem {idade} anos em {anoAtual}')
        if idade == 18:
            print('Está na hora de alistar.')
        elif idade < 18:
            print(f'Ainda faltam {18 - idade} anos para se alistar. Seu alistamento será em {(18 - idade) + anoAtual}')
        else:
            print(f'Já passou da hora de alistar! Você deveria ter se alistado há {idade - 18} anos. O ano do seu alistamento foi {anoNasc +18}.')

