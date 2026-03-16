#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
#deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite a expressão: '))
parentese = list()
#varre a lista
for caractere in expressao:
    #checa se o parêntese foi aberto
    if caractere in '(':
        parentese.append(caractere)
    #checa se existe algum parêntese aberto
    if parentese.count('(') > 0:
        #caso a condição acima seja verdadeira, e o usuario fechar o parentese, ele remove a abertura de parêntese,
        #indicando que abriu e fechou corretamente
        if caractere in ')':
            parentese.remove('(')
    #Caso não haja parêntese aberto
    else:
        # se o usuário tentar fechar um parêntese ele irá adicionar o fechamento, tornando a expressão errada
        if caractere in ')':
            parentese.append(')')
if len(parentese) == 0:
    print('Essa é uma expressão válida.')
else:
    print('Essa não é uma expressão válida.')