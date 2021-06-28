idade = idadeM = homens = mulheres = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    i = int(input('IDADE: '))
    s = ' '
    while s not in 'MF':                                                   # este comando serve para caso o usuário
        s = str(input('SEXO [M/F]: ')).strip().upper()[0]                  # digite um valor não pedido
    print('-' * 30)
    if i >= 18:
        idade += 1
    if s == 'M':
        homens += 1
    if s == 'F' and i < 20:
        mulheres += 1
        idadeM += 1
    con = ' '
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if con == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {idade}')
print(f'Ao todo temos {homens} homen(s) cadastrado(s)')
print(f'E temos {mulheres} mulher(es) com menos de 20 anos')
