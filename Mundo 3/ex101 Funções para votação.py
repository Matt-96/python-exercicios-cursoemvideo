#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.
def voto(ano):
    """
    Recebe um ano de nascimento e diz se uma pessoa deve ou não votar.
    :param ano: Utilizado para calcular a idade e com base nisso o tipo de voto
    :return: Retorna uma string formatada com idade e tipo de voto
    """
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - ano

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
