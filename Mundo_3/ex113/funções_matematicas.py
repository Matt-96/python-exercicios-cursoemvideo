#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
#digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    from colorama import Fore,  init
    init(autoreset=True)
    while True:
        try:
            n = input(msg)
            return  int(n)
        except ValueError:
            print(Fore.RED + 'ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print(Fore.RED + 'O usuário preferiu não informar esse valor')
            break



def leiaFloat(msg):
    from colorama import Fore,  init
    init(autoreset=True)
    while True:
        try:
            n = input(msg).strip().replace(',', '.')
            return float(n)
        except ValueError:
            print(Fore.RED + 'ERRO! Digite um número float válido.')
        except KeyboardInterrupt:
            print(Fore.RED + 'O usuário preferiu não informar esse valor')
            break

