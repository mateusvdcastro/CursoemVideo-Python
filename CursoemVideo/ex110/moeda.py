def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)       # é o mesmo que estava sendo escrito antes mas de outra forma


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$', format=False):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço, aument, dimin):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aument}% de aumento: \t{aumentar(preço, aument, True)}')
    print(f'{dimin}% de desconto: \t{aumentar(preço, dimin, True)}')        # \t é tabulação
    print('-'*30)


