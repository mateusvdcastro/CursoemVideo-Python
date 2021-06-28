from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for v in range(0, 5):
        n = randint(1, 10)
        print(n, end=' ')
        numeros.append(n)
    print('PRONTO!')


def somaPar(lista):
    global cont   # ou só colocar o cont = 0 dentro da def
    for i, v in enumerate(lista):
        if v % 2 == 0:
            cont += v
    print(f'Somando os valores pares de {numeros}, temos {cont}')


# programa principal
cont = 0
numeros = list()
sorteia(numeros)
somaPar(numeros)
