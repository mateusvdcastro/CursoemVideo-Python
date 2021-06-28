cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezeoito',
        'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 a 20:'))
    if 0 <= n <= 20:
        print(f'Você digitou o número {cont[n]}')
    next = ' '
    while next not in 'SN':
        next = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if next == 'N':
        break
