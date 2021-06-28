n = int(input('Digite um número: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi dividido {total} vezes')
if total == 2:
    print('O número é Primo!!!')
else:
    print('O número não é Primo!!!')

