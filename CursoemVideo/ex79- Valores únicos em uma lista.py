lista = []
l = []
while True:
    lista.append(int(input('Digite um valor: ')))
    for v in lista:
        if v not in l:
            l.append(v)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'Você digitou os valores {sorted(l)}')
l.sort(reverse=True)
print(f'Agora o inverso {l}')

'''# a função set() retira as repetições de uma lista
lu = list(set(lista))
print(lu)                             # ver ex 80'''
