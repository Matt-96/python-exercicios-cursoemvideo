from colorama import Fore, init
init(autoreset=True)
def leiaDinheiro(msg):
    while True:
        valor = input(msg).strip().replace(',', '.')

        if valor.isalpha() or valor.strip() == '':
            print(f'{Fore.RED}"{valor}" é um preço inválido.')
        else:
            return float(valor)


