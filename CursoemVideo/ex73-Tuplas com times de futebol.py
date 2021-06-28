# tuplas são ruins pr esse tipe de código pois são imutáveis, porém era o conhecimento do momento
times = ('Atlético-MG', 'Internacional', 'Flamengo', 'São Paulo', 'Fluminense', 'Santos', 'Palmeiras',
         'Fortaleza', 'Sport Recife', 'Vasco da gama', 'Ceará SC', 'Atlético GO', 'Botafogo', 'Grêmio',
         'Athletico PR', 'Bahia', 'Corinthians', 'Coritiba', 'Bragantino SP', 'Goiás')
print('-='*30)
print(f'Lista de times do brasileirão: {times}')
print('-='*30)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*30)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*30)
cont = len(times)
print(f'O São Paulo está na {times.index("São Paulo")+1}ª posição ') # usar aspas duplas, pois ele está dentro das aspas simples do format, assim ele entende a interpolação
