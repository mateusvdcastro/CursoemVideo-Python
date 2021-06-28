def fatorial(num, show=False):
    """
    -> Cálcula o Fatorial de um Número
    :param num: O número a ser cálculado
    :param show: (opcional) mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    """
    fat = 1
    for n in range(num, 0, -1):
        if show:
            print(n, end='')
            if n > 1:
                print(f' x ', end=' ')
            else:
                print(' = ', end='')
        fat *= n
    return fat


print(fatorial(5, show=True))
print()
help(fatorial)
