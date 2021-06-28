temp = []
pricipal = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    # [:] faz a cópia da lista e não gera uma ligação entre elas
    if len(pricipal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    pricipal.append(temp[:])
    temp.clear()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print(pricipal)
print(f'Ao todo você cadastrou {len(pricipal)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in pricipal:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in pricipal:
    if p[1] == men:
        print(f'[{p[0]}]', end='')

'''INPUT SEM CLEAR DA LISTA:
    guys.append ( [ input('Digite o nome ') ,  float ( input('Digite o peso') ) ] )'''
