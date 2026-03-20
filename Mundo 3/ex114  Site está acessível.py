#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request
import urllib.error
from colorama import init, Fore
init(autoreset=True)

try:
    headers = {'user-Agent':'Mozilla/5.0'}
    req = urllib.request.Request('https://www.pudim.com.br', headers=headers)
    site = urllib.request.urlopen(req)
except urllib.error.URLError:
    print(Fore.RED + 'O site pudim está offline')
else:
    print(Fore.GREEN + f'O site pudim está online')