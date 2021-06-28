# ranking de países com maior PIB

print('='*100)
cont = 0
rp = ('EUA','União Europeia','China','Japão','Alemanha','Índia','Reino Unido','França','Itália','Brasil','Canadá','Rússia','Coreia do Sul','Espanha','Austrália','México','Indonésia','Holanda','Arábia Saudita','Turquia')
print(f'Ranking dos 5 primeiros países: \n1° lugar: {rp[0]}\n2° lugar: {rp[1]}\n3° lugar: {rp[2]}\n4° lugar: {rp[3]}\n5° lugar: {rp[4]}')
print(f'Os último 5 colocados são: \n15° lugar: {rp[-6]}\n16° lugar: {rp[-5]}\n17° lugar: {rp[-4]}\n18° lugar: {rp[-3]}\n19° lugar: {rp[-2]}\n20° lugar: {rp[-1]}')
b = rp.index('Brasil')
print(f'O Brasil está na {b+1}° posição.')
print('-'*100)
print('Lista completa abaixo:')
for r in range (0,len(rp)):
    print('-'*100)
    print(f'{(cont) + 1}° lugar: {rp[cont]}')
    cont += 1