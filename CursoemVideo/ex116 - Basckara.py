import math


def Bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return (None, None)  # Raiz Negativa
    x = math.sqrt(delta)
    x1 = (-b + x) / (2 * a)
    x2 = (-b - x) / (2 * a)
    return x1, x2


if __name__ in '__main__':
    a = int(input('Digite um valor para A: '))
    b = int(input('Digite um valor para B: '))
    c = int(input('Digute um valor para C: '))
    x = Bhaskara(a, b, c)
    print('X1 = {}'.format(x[0]))
    print('X2 = {}'.format(x[1]))
