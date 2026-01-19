#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 #Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


casa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o salário do comprador R$:'))
anos = int(input('Digite  em quantos anos irá pagar: '))

prestaçao = casa / (anos * 12)

print(f'Para pagar uma casa no valor de R${casa:.2f} em {anos} anos o valor da prestação será R${prestaçao:.2f}. ')

if prestaçao > salario * 0.30:
    print('EMPRESTIMO NEGADO.')
else:
    print('EMPRESTIMO APROVADO.')

