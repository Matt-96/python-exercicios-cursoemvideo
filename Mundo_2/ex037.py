#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e
#peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.



num = int(input('Digite um número inteiro: '))
opcao = str(input('Escolha uma das bases para conversão: \n'
            '[ 1 ] Converter para Binário\n'
            '[ 2 ] Converter para Octal\n'
            '[ 3 ] Converter para Hexadecimal\n'
                  'Sua Opção:'))
if opcao == '1':
    print(f'{num} convertido para Binário é igual a {bin(num)}')
elif opcao == '2':
    print(f'{num} convertido para Octal é igual a {oct(num)}')
else:
    print(f'{num} convertido para Hexadecimal é igual a {hex(num)}')