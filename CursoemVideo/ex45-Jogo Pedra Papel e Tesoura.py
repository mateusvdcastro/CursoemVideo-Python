from time import sleep
from random import randint
print('Suas opções:')
print('''[0]Pedra
[1]Papel
[2]Tesoura''')
itens = ('Pedra','Papel','Tesoura')
e = int(input('Qual sua opção?: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
n = randint(0,2)
print('-='*20)
print(f'O computador escolheu {itens[n]}')
print(f'O jogador escolheu {itens[e]}')
print('-='*20)
if n == 0:
    if e == 0:
        print('Empate')
    elif e == 1:
        print('Jogador venceu')
    elif e ==2:
        print('Computador Venceu')
    else:
        print('Jogada inválida')
elif n == 1:
    if e == 0:
        print('Computador venceu')
    elif e == 1:
        print('EMPATE')
    elif e ==2:
        print('Jogador Venceu')
    else:
        print('Jogada inválida')
elif n == 2:
    if e == 0:
        print('Jogador venceu')
    elif e == 1:
        print('Computador venceu')
    elif e ==2:
        print('EMPATE')
    else:
        print('Jogada inválida')
