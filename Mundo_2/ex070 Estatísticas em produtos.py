#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
tot_prod = prod_mais1000 = cont = barato = 0
barato_nome = ''
while True:
    cont += 1
    resp = ' '
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    #Uso essa condição para definir o primeiro mais barato
    if cont == 1:
        barato = preço
        barato_nome = produto
    #Aqui eu faço as comparações, e no caso de haver um preço menor eu atribuo a var barato.
    else:
        if barato > preço:
            barato = preço
            barato_nome = produto
    #Soma o preço dos produtos
    tot_prod += preço
    #Verifica se tem produto que custa mais de R$1000
    if preço > 1000:
        prod_mais1000 += 1

    #Valida se o usuário está digitando corretamente
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S / N]: ')).strip().upper()[0]
    #Encerra o programa caso o usuário não queira mais cadastrar produtos
    if resp == 'N':
        break
print(f'No total foram gastos R${tot_prod:.2f}.')
print(f'Foram comprados {prod_mais1000} produtos acima de R$1000.')
print(f'O nome do produto mais barato é {barato_nome} e ele custa {barato:.2f}')