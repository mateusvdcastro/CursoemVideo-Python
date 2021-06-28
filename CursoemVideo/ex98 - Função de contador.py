from time import sleep
# solução do Professor


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(1)
            cont -= p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)


'''def contador(i, f, p):
    print(f'Contando de {i} até {f} de {p} em {p}')
    if i > f:
        if p > 0:
            p *= -1
        else:
            p = p
    for c in range(i, f+1, p):
        print(c, end=' ')
    print('Fim')
    print('-='*30)


contador(1, 10, 1)
contador(10, 0, 2)
contador(i=int(input('Início: ')), f=int(input('Fim:  ')), p=int(input('Passo:  ')))'''


