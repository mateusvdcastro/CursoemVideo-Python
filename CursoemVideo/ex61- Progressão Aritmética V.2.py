print('Gerador de PA\n', '=-=' * 10)
n = 0
n1 = int(input('Primeiro termo: '))
razão = int(input('Qual a razão?: '))
while n < 10:
    n = n +1
    an = n1 + (n-1)*razão
    print(an, end='')                                        # Para esse programa bastava mostrar os 10 primeiros termos
    print(' - ' if n < 10 else ' ', end='')                  # Três maneiras de fazer

print()

for n in range(1, 11):
    an = n1 + (n-1)*razão
    print(an, end='')
    print(' - ' if n < 10 else ' ', end='')

print()

n1 = int(input(f'Qual o primeiro termo?: '))
razão = int(input('Qual a razão da PA?: '))
cont = 1
termo = n1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo = termo + razão
    cont = cont + 1
print('Pausa')
