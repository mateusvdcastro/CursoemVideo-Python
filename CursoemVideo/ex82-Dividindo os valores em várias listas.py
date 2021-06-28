lista = []
listapar = []
listaimp = []
while True:
    lista.append(int(input('Digite um número: ')))
    count = ' '
    while count not in 'SN':
        count = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if count == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimp.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimp}')
