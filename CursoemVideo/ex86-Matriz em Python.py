# solução do guanabara
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para {[l,c]}: '))
print('-='* 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


# minha solução
'''matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        v = int(input(f'Digite o valor para {[l,c]}: '))
        matriz[l].append(v)
for l in matriz:
    print(l)'''
