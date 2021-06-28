salario = float(input('Qual o salário do funcionário: '))
if salario <= 1250:
    novo = salario*1.15
else:
    novo = salario*1.1
print(f'Quem ganhava R${salario} agora passa a ganhar R${novo}')
