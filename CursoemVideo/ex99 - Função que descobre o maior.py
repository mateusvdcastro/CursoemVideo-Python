def maior(*val):
    cont = mai = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in val:
        print(f'{valor} ', end='')
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'Foram analisados {len(val)} valores ao todo.')
    print(f'O maior valor informado foi {mai}')


maior(2, 5, 6, 8)
maior(2, 3)
maior(6)
maior()
