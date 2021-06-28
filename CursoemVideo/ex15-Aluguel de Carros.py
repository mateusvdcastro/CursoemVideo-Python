km = float(input('Quantos Km foram rodados?: '))
dia = float(input('Por quantos dias ele foi alugado?: '))
total = (km * 0.15) + (dia * 60)
print(f'O total a pagar é de: R$ {total:.2f}')
