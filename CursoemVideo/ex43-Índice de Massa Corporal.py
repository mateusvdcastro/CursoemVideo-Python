peso = float(input('Qual o seu peso? (Kg): '))
h = float(input('Qual a sua altura? (m): '))
imc = peso / (h * h)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print('Você está', end=' ')
    print('Abaixo do Peso')
elif imc < 25:
    print('Você está com o', end=' ')
    print('Peso ideal')
elif imc < 30:
    print('Você está com', end=' ')
    print('Sobrepeso')
elif imc <= 40:
    print('Você está', end=' ')
    print('Obesidade')
else:
    print('Você está', end=' ')
    print('Obesidade Mórbida')
