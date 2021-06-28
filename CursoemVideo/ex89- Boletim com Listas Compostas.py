ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('NOta 2: '))
    média = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], média])
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'{"Nº":<4} {"Nome":<10} {"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')
while True:
    print('-'*30)
    val = int(input('Mostrar notas de qual aluno? (digite 999 para interromper): '))
    if val == 999:
        print('Finalizando...')
        break
    if val <= len(ficha)-1:
        print(f'Notas de {ficha[val][0]} são {ficha[val][1]}')
print('<<<Volte Sempre>>>')


'''
# Minha solução
lista = []
principal = []
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('NOta 2: ')))
    principal.append(lista[:])
    lista.clear()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'{"Nº":<3} {"Nome":<3} {"Média":>8}')
for i, v in enumerate(principal):
    média = (v[1] + v[2])/2
    print(f'{i:<3} {v[0]:<3} {média:>8}')
print('-='*30)
while True:
    val = int(input('Mostrar notas de qual aluno? (digite 999 para interromper): '))
    if val == 999:
        break
    for i, v in enumerate(principal):
        if val == i:
            print(f' As notas de {v[0]} [{v[1]}, {v[2]}]')
print('-='*30)
'''
