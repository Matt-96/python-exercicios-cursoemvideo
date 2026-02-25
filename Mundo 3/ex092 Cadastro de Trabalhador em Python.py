#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
#em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
anoAtual = datetime.today().year

trabalhador = dict()

trabalhador['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = anoAtual - nasc
trabalhador['CTPS'] = int(input('Carteira de trabalho: (0 não tem)'))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    #Calcula a idade que tinha quando foi contrato e soma o tempo de contribuição
    trabalhador['Aposentadoria'] = (trabalhador['Contratação'] - nasc) + 35
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}.')