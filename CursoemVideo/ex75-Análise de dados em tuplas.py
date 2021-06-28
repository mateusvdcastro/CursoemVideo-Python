import math
num = (int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'O 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'O primeiro 3 está na posição {num.index(3,0)+1} ')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

