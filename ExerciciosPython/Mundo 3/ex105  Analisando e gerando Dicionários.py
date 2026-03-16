#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:

#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação (opcional)

#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(*num,sit=True):
    """
    Cria um dicionário contendo as notas de uma turma e suas informações(quantidade de notas, maior e menor nota, media
    e situação se solicitado.
    :param num: Recebe um quantidade ilimitada de notas
    :param sit: Calcula a situação da turma
    :return: Retorna o dicionario com as notas e informações cadastradas.
    """
    turma = dict()

    turma['total'] = len(num)
    turma['maior'] = max(num)
    turma['menor'] = min(num)
    turma['media'] = sum(num) / turma['total']
    if sit:
        if turma['media'] <= 5:
            turma['situação'] = 'RUIM'
        elif 5 < turma['media'] < 7.4:
            turma['situação'] = 'REGULAR'
        else:
            turma['situação'] = 'BOA'
    return turma


#Programa principal
resp = (notas(6.6, 6.7,9.5))
print(resp)