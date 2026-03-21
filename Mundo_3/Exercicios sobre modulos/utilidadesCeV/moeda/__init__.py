def metade(preço,show=True):
    res = preço / 2
    if show:
        return moeda(res)
    else:
        return res

def dobro(preço, show=True):
    res = preço * 2
    if show:
        return moeda(res)
    else:
        return res

def aumentar(preço, taxa, show=True):
    res = (preço * taxa/100) + preço
    if show:
        return moeda(res)
    else:
        return res


def diminuir(preço, taxa, show=True):
    res = preço - (preço * taxa/100)
    if show:
        return moeda(res)
    else:
        return res

def moeda(preço=0, moeda='R$'):
    res = f'{moeda}{preço:.2f}'.replace('.',',')
    return res


def resumo(preço=0, taxa_a=20, taxa_r=12):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(preço):>10}')
    print(f'{"Dobro do preço:":<20}{dobro(preço, True):>10}')
    print(f'{"Metade do preço:":<20}{metade(preço, True):>10}')
    # Note a dinamicidade abaixo:
    print(f'{f"{taxa_a}% de aumento:":<20}{aumentar(preço, taxa_a, True):>10}')
    print(f'{f"{taxa_r}% de redução:":<20}{diminuir(preço, taxa_r, True):>10}')
    print('-' * 30)