#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('=' * 11, ' LOJAS BARATÃO ', '=' * 11)

preço = float(input('Preço das Compras:R$'))
opção = int(input('FORMAS DE PAGAMENTO \n '
                  '[ 1 ] à vista dinheiro/cheque \n'
                  '[ 2 ] à vista cartão \n'
                  '[ 3 ] 2X no cartão \n'
                  '[ 4 ] 3x ou mais no cartão \n '
                  'Qual a sua opção? '))

if opção == 1:
    desc = preço - (preço * 0.10)
    print(f'Sua compra no valor de R${preço:.2f} vai custar R${desc:.2f} no final. ')
elif opção == 2:
    desc = preço - (preço * 0.05)
    print(f'Sua compra de R${preço:.2f} vai custar R${desc:.2f} no final.')
elif opção == 3:
    valorParcela = preço / 2
    print(f'Sua compra de R${preço:.2f} não vai sofrer alteração no preço final. O pagamento será efetuado em 2 parcelas de R${valorParcela:.2f}')
elif opção == 4:
    parc = int(input('Em quantas parcelas deseja pagar? (Máx 10.)'))
    if parc > 10:
        print('Número de parcelas inválido. Sua compra foi cancelada.')
    else:
        juros = preço + (preço * 0.20)
        valorParcela = juros / parc
        print(f'Sua compra de R${preço:.2f} vai custar R${juros:.2f} no final. O pagamento será efetuado em {parc} parcelas de R${valorParcela:.2f}')
else:
    print('Opção inválida. Compra cancelada.')



