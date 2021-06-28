n = int(input('Digite um número da tábuada: '))
for h in range(1, 11):
    p = h
    for c in range(1):
        print(f'{n} X {p:2} = {n * p}')
print('')

# duas formas de se fazer uma tábuada

o = int(input('Digite um número da tábuada: '))
for c in range(1,11):
    print(f'{o} X {c:2} = {o*c}')
