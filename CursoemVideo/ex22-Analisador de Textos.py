#.strip() para eliminar os espaços da direita e esquerda que o usuario digitar, evitando erro na linha 6. Além da função  - (nome.cont(" "))
# para tirar os espaços entre um nome e outro. Linha 6
nome =str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em Maiúsculas é: {nome.upper()}')
print(f'Seu nome em Minúsculas é: {nome.lower()}')
print(f'O seu nome ao todo tem: {len(nome) - (nome.count(" "))} Letras')
#duas formas de fazer as linhas 9 e 10.
#print(f'Seu primeiro nome tem {nome.find(" ")} Letras')
print(f'O seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} Letras')
