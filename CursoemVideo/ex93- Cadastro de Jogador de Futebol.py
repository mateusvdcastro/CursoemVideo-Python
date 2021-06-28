dados = dict()
gols = list()
dados['Nome'] = str(input('Digite o nome do jogador: '))
part = int(input(f'Quantas partidas {dados["Nome"].capitalize()} jogou?: '))
for c in range(0, part):
    gol = int(input(f'Quantos Gols na partida {c}: '))
    gols.append(gol)
dados['Gols'] = gols[:]
dados['Total'] = sum(gols)     # para calcular o tot dos numeros na lista
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {dados["Nome"].capitalize()} jogou {len(dados["Gols"])} jogos.')
# for i, v in enumerate(dados['Gols']): Ou fazer dessa forma
for v in range(0, len(dados['Gols'])):
    print(f'  => Na partida {v}, fez {dados["Gols"][v]}')
