#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso (KG): '))
altura = float(input('Digite sua altura(m): '))
imc =  peso / (altura ** 2)


print(f'Seu IMC é de {imc:.2f} ')

if imc <18.5:
    print('Categoria: Abaixo do peso.')
elif imc < 25:
    print('Categoria: Peso Ideal')
elif imc < 30:
    print('Categoria: Sobrepeso')
elif imc < 40:
    print('Categoria: Obesidade')
else:
    print('Categoria: Obesidade Mórbida')