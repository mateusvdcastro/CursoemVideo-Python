d = float(input('Qual a distancia da sua viagem?: '))
if d <= 200:
    d1 = d*0.5
    print(f'Você está prestes a começar uma viagem de {d}KM')
    print(f'E o preço da sua passagem será R${d1}')
else:
    d2 = d*0.45
    print(f'Você está prestes a começar uma viagem de {d}KM')
    print(f'E o preço da sua passagem será R${d2}')

'''d1 = d * 0.5
d2 = d * 0.45
print(f'Você está prestes a comecar uma viagem de {d} e o preço da sua passagem será {d1}') if d <= 200 else  print(f'Você está prestes a comecar uma viagem de {d} e o preço da sua passagem será {d2}')'''