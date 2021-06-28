n=int(input('Informe um número: '))
print(f'Analisando o número {n}: ')
# % é uma divisão do resto 1943 % 10 = 3 porque dá 194,3.
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar {m}')
