#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
from operator import index

times = ('Botafogo', 'Chapecoense','Vitória','Fluminense','Mirassol','Bahia','São Paulo','Atlhletico-PR','Bragantino',
         'Palmeiras','Atlético-MG','Flamengo','Grêmio','Corinthians','Vasco','Coritiba','Internacional','Santos','Remo',
         'Cruzeiro')
print('=-=' * 10)
print(f'Lista de times do Brasileirão:{times}')
print('=-=' * 10)
print(f'Os 5 primeiros são:{times[0:5]} ')
print('=-=' * 10)
print(f'Os 4 últimos são:{times[-4:]}')
print('=-=' * 10)
print(f'Times em ordem alfabética:{sorted(times)}')
print('=-=' * 10)
print(f'A Chapecoense está na {times.index('Chapecoense')+1}º posição')
