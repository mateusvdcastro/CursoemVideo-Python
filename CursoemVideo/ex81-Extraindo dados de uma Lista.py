lista = []
while True:
    lista.append(input('Digite um valor:'))
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são ', end='')
for v in lista:
    print(v, end=' ')
print()
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
