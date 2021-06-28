s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]               #pegar só a primeira letra
while s not in 'MF':
    s = str(input('Dados inválidos. Informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {s} registrado com sucesso!')
