# color rise--- pesquisar
print('\033[4;30;45mOlá mundo!\033[m')
print('\033[7;30mAprendendo Cores!\033[m')
print('\033[7;33;44mTeste inverter com a tecla 7!\033[m')
a = 5
b = 10
print(f'O valor \033[32m{a}\033[m e \033[31m{b}\033[m!!!')
nome = 'Mateus'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

# Forma mais organizada de fazer o código acima
cores = {'pretoebranco':'\033[7;30m',
         'Limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['Limpa']))

