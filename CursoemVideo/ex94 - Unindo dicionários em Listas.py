galera = list()
dados = dict()
soma = média = 0
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if dados['Sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F! ')
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    galera.append(dados.copy())
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(galera)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas!')
média = soma / len(galera)
print(f'B) A média das idades é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"].capitalize()} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<Encerrado>>')
