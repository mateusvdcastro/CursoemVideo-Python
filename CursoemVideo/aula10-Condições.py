n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print(f'Sua média foi de {m}')
if m >= 6:
    print('Sua média foi boa, PARÁBENS!!')
else:
    print('Sua média foi ruim, estude mais.')
# forma simplificada de fazer a condicional
print('Parabéns' if m >= 6 else 'Estude mais!')

