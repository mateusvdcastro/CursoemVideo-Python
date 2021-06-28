print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
a1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for c in range(1, 11):
    p = a1 + razão*(c-1)
    print(f'{p}', end=' → ') # Para colocar a seta apertar alt + 26
print('ACABOU')
