def área(comprimento, largura):
    a = comprimento * largura
    print(f'A área de um terreno de {comprimento}X{largura} tem área de {a}m²')


# Programa principal
print('Controle de terreno')
print('-'*20)
l = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do Terreno (m): '))
área(c, l)
