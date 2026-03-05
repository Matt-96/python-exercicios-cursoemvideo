#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.

def ficha(nome = '<desconhecido>',gols=0):

    return f'O jogador {nome} fez {gols} gols.'


#Programa principal
nome_jogador = str(input('Nome do jogador: '))
gols_qtd = str(input('Número de gols: '))
if gols_qtd.isnumeric():
    gols_qtd = int(gols_qtd)
else:
    gols_qtd = 0
if nome_jogador == '':
    nome_jogador = '<desconhecido>'
print(ficha(nome_jogador,gols_qtd))
