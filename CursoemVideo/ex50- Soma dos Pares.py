s = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º numero:'))
    if n % 2 == 0:
        s += n
print(f'A soma dos números pares entre os mencionados é {s}')
