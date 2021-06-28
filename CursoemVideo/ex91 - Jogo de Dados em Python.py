from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k}: tirou {v} no dado')
    sleep(0.4)
# utilizamos o itemgetter para ordenar os valores do dicionário e exibir as colocações
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# itemgetter(0) fica em ordem de chave e se for itemgetter(1) fica em valor
print('-='*30)
print('  == RANKING DOS JOGADORES ==  ')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.4)
