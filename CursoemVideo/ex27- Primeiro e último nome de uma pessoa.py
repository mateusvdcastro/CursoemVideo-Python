nome = str(input('Digite o seu nome completo: ')).strip()
print('Prazer em te conhecer!')
print(f'O seu primeiro nome é {nome.split()[0]}')
print(f'O seu último nome é {nome.split()[-1]}')