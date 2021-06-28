from random import randint
v = 0
print('-=' * 20)
print('Vamos jogar par ou ímpar')
print('-=' * 20)
while True:
    n = int(input('Digite um número: '))
    pi = ' '
    c = randint(0, 10)
    total = n + c
    while pi not in 'PI':                                             # esse While serve para caso o usuário não digite nem P nem I, assim ele irá perguntar novamente
        pi = str(input('Par ou Ímpar?: [P/I] ')).strip().upper()[0]
    print(f'Você digitou {n} e o computador {c}, no total {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if total % 2 == 0:
        if pi == 'P':
            print('Você venceu!!')
            v += 1
        else:
            print('Você Perdeu')
            break
    else:
        if pi == 'I':
            print('Você venceu!!')
            v += 1
        else:
            print('Você Perdeu!!')
            break
    print('Jogue novamente!!')
    print('--' * 30)
print(f'Você venceu {v} vezes')
