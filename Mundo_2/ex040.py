#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO


nota1 = float(input('Digite a 1° nota do aluno: '))
nota2 = float(input('Digite a 2º nota do aluno: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('REPROVADO! ESTUDE MAIS!')
elif 5 <= media <7:
    print('RECUPERAÇÃO! QUASE LÁ. SE ESFORCE MAIS UM POUCO.')
else:
    print('APROVADO! PARABÉNS!')