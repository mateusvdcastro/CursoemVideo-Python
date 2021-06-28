listagem = ('Régua', 4,
            'Estojo', 6,
            'Lápis', 0.30,
            'Apontador', 0.5,
            'Esquadro', 5,
            'Xerox', 0.20,
            'Bala', 1,
            'Telescópio', 2560)
print('-'*40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:                                # pois os nomes estão em posições pares dentro da tupla listagem
        print(f'{listagem[pos]:.<30} ', end='')
    if pos % 2 != 0:                                # pois os numeros estão em posições ímpares na tupla listagem
        print(f'R$ {listagem[pos]:>7.2f}')
print('-'*40)
