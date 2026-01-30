while True:
    num = int(input('Quer ver a tabuada de qual valor ? '))
    cont = 0
    if num < 0:
        break
    print('-' * 20)
    for cont in range(1, 11):

        print(f'{num} X {cont} = {num * cont}')
    print('-' * 20)

