listadegols = []
dicionario = {}
final = []
while True:
    listadegols.clear()
    dicionario.clear()
    dicionario['Nome'] = str(input('Nome do jogador: ')).strip()
    vezes = int(input(f'Quantas partidas {dicionario["Nome"].capitalize()} jogou?: '))
    for c in range(0, vezes):
        gol = int(input(f'Quantos gols {dicionario["Nome"].capitalize()} jogou na {c+1}ª partida?: '))
        listadegols.append(gol)
    dicionario["Gols"] = listadegols[:]
    dicionario['Total'] = sum(listadegols)
    final.append(dicionario.copy())
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'cod ', end='')
for i in dicionario.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for i, v in enumerate(final):
    print(f'{i:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-'*30)
while True:
    jogador = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if jogador == 999:
        break
    if jogador >= len(final):
        print('Erro! Não existe jogador com esse número')
    else:
        print(f'-- Levantamento do jogador {final[jogador]["Nome"].capitalize()}')
        for i, v in enumerate(final[jogador]['Gols']):
            print(f'    Na partida {i+1} fez {v} gols.')
    print('-'*30)
print('<<<Volte sempre>>>')
