from os import write

from Mundo_3.ex115.interface import cabecalho


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
        try:
            arq = open(nome, 'wt+')
            arq.close()
        except:
            print('Houve um erro na criação do arquivo')
        else:
            print(f'{nome} criado com sucesso')

def ler_arquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arq:
            dados = linha.strip().split(';')
            if len(dados) > 1:
                print(f'{dados[0]:<30} {dados[1]:>3} anos')

def cadastro_pessoa(nome, pessoa='desconhecido', idade=0):
    try:
        #esse comando abre e fecha o arquivo
        with open(nome,'at') as a:
            #esse comando escreve os dados capturados pelo input do programa principal
            a.write(f'{pessoa};{idade}\n')
    except:
        print('Houve um ERRO ao escrever os dados!')
    else:
        print(f'Novo registro de {pessoa} adicionado.')

