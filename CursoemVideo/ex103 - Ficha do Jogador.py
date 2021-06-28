def ficha(n='<Desconhecido>', g =0):
    print(f'O jogador {n.capitalize()} fez {g} gol(s).')
    print('-' * 40)



n = str(input('Qual o nome do Jogador?'))
g = str(input('Quantos gols?'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(g=g)
else:
    ficha(n, g)


''''# solução de um coment
def ficha(nome='desconhecido', gol=0):
    if nome == '':
        nome = '<desconhecido>'
    if not gol.isnumeric():
        gol = '0'
    return f'O jogador {nome} fez {gol} gols no campeonato'''


'''jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
ficha(jogador, gols)'''
