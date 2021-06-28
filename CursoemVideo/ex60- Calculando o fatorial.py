from math import factorial
n = int(input('Digite um número para cálcular seu fatorial: '))
f = factorial(n)
print(f'Calculando {n}! = {f}')


# outro jeito de resolver
n = int(input('Digite um número para cálcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! =', end=' ')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f'{f}')

n = int(input('Digite um número para cálcular seu fatorial: '))
print(f'Calculando {n}! = ', end=' ')
f = 1
for n in range(n, 0, -1):
    print(n, end=' ')
    print(' X ' if n > 1 else ' = ', end=' ')
    f = f * n
print(f)
