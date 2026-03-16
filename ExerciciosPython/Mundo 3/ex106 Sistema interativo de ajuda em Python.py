#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e
# o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
from time import sleep
c = (
    '\033[m',  # 0 - Reset
    '\033[1;97;41m',  # 1 - Branco + Vermelho
    '\033[1;97;42m',  # 2 - Branco + Verde
    '\033[1;30;44m',  # 3 - Preto + Azul (Melhor contraste que branco no azul)
    '\033[1;30;107m',  # 4 - Preto + Branco Total (Manual)
    '\033[1;97;45m'  # 5 - Branco + Roxo
)


def escreva(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')  # Ativa a cor escolhida
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')  # Reseta para não pintar o input
    sleep(1)


def ajuda(com):
    escreva(f'Acessando o manual do comando "{com}"', 3)
    print(c[4], end='')  # Ativa fundo branco para o manual
    help(com)
    print(c[0], end='')  # Reseta após o manual
    sleep(2)

# Programa Principal
while True:
    escreva('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).strip().lower()

    if comando == 'fim':
        escreva('ATÉ LOGO!', 1)
        break

    ajuda(comando)