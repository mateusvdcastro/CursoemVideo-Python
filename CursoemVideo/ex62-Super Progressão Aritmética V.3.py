n1 = int(input(f'Qual o primeiro termo?: '))
razão = int(input('Qual a razão da PA?: '))
n = 0
vezes = 0
cont = 1
mais = 10
while mais != 0:
    nt = n + mais
    while n < nt:
        n = n + 1
        an = n1 + (n-1)*razão
        cont = cont + an
        print(an, end='')
        print(' - ' if n < nt else ' = ', end=' ')
        vezes = vezes + 1
    print(cont)
    mais = int(input('Quantos termos a mais você quer exibir?: '))
print(f'Finalizado com {nt} termos')
print('FIM')



