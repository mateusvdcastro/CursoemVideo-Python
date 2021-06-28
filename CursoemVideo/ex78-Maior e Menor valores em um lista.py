'''valores = []
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
print('-'*40)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} e está na posição {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} e está na posição {valores.index(min(valores))}')'''

# ou, porém exibindo todas as posições caso o número repita

valores1 = []
maior = menor = 0
for pos in range(0, 5):
    valores1.append(int(input(f'Digite um valor para a posição {pos}: ')))
    if pos == 0:
        maior = menor = valores1[pos]
    else:
        if valores1[pos] > maior:
            maior = valores1[pos]
        if valores1[pos] < menor:
            menor = valores1[pos]
print('-'*40)
print(f'Você digitou os valores {valores1}')
print(f'O maior valor é {maior} e sua posição é', end=' ')
for indice, valor in enumerate(valores1):
    if valor == maior:
        print(f'{indice}....', end='')
print()
print(f'\nO menor valor é {menor} e sua posição é', end=' ')
for indice, valor in enumerate(valores1):
    if valor == menor:
        print(f'{indice}....', end=' ')
print()
