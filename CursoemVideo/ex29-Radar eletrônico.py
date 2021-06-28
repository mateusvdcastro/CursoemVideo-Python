velo = float(input('Qual a velôcidade atual do carro? '))
if velo <= 80:
    print('Tenha um bom dia dirija com segurança.')
else:
    m = (velo-80)*7
    print(f'Você foi MULTADO, excedeu o limite de 80 KM/H.')
    print(f'Você deve pagar uma multa no valor de R${m:.2f}.')

