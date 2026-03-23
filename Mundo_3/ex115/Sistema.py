from Mundo_3.ex113.funções_matematicas import leiaInt
from interface import menu, cabecalho
from time import sleep
from colorama import init, Fore
from arquivo import *
init(autoreset=True)

arquivo = 'cadastro.txt'

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)
while True:
    sleep(1)
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa', 'Sair do Sistema'])
    #Opção de listar o conteúdo do arquivo
    if resposta == 1:
        ler_arquivo(arquivo)


    elif resposta == 2:
        cabecalho('OPÇÃO 2')
        try:
            while True:
                nome = str(input('Nome:'))
                if nome.isalpha():
                    break
                print('Digite um nome válido.')
            while True:
                idade = leiaInt('Idade:')
                if idade > 0:
                    break
                print('Digite uma idade válida.')
        except:
            print('Algo deu errado. Tente novamente.')
        else:
            cadastro_pessoa(arquivo, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo do Sistema ... Até logo!')
        break
    else:
        print(Fore.RED +  'Digite uma opção válida!')



