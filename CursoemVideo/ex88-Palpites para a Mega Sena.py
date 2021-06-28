from random import randint

print('-=' * 30)
print('JOGO DA MEGA SENA'.center(30))
print('-=' * 30)
tot = 1
jogos = []
lista = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}º: {l}')

'''
# resolução nos comentários
from random import sample
from time import sleep

jogos = list()
n = int(input('Quantos jogos?: '))
for c in range(n):
    a = sorted(sample(range(1, 61), 6))
    jogos.append(a[:])
    print(f'Jogo {c + 1}: {a}')
    sleep(0.5)
'''

# Minha solução
'''from random import randint
print('-='* 30)
print('JOGO DA MEGA SENA'.center(30))
print('-='* 30)
jogos = int(input('Quantos jogos você quer que eu sorteie?: '))
print(f'Sortendo {jogos} jogos')
for c in range(0, jogos):
    lista = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f'Jogo {c+1}: {lista}')
'''
