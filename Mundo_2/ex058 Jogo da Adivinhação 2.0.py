#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
#Essa variável faz o computador "pensar"
comp = randint(0, 10)
tentativas = 0
acertou = False
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar??
''')

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    tentativas += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador > comp:
            print('Menos... Tente mais uma vez.')
        else:
            print('Mais... Tente novamente.')

print(f'Eu pensei {comp} e você chutou {jogador}. Parabéns, você acertou. Foram necessárias {tentativas} tentativas'
      f' para você acertar. ')