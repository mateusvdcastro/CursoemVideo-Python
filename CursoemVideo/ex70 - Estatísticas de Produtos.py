total = maisdemil = menor = vezes = 0
menorNP = ''
print('-' * 30)
print('Loja baratão')
print('-' * 30)
while True:
    nome = str(input('Digite o nome do Produto: ')).strip().capitalize()
    preço = float(input('Preço R$: '))
    vezes += 1
    if vezes == 1:
        menor = preço
        menorNP = nome
    else:
        if preço < menor:
            menor = preço
            menorNP = nome
    cont = ' '
    total += preço
    if preço >= 1000:
        maisdemil += 1
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('FIM DO PROGRAMA!!!')
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {maisdemil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi a/o {menorNP} que custa {menor}')

''' if vezes == 1:
        menor = preço
        menorNP = nome
    else:
        if preço < menor:
            menor = preço
            menorNP = nome'''
   # essa passagem pode ser simplificada por 'or':
''' if vezes == 1 or preço < menor:
        menor = preço
        menorNP = nome'''
'''   # código de um comentário no youtube 
from math import fsum
lista_produtos = []
lista_preços = []
produtos_1000 = 0
while True:
    produto = str(input("Qual o nome do produto?"))
    lista_produtos.append(produto)
    preço = float(input("Qual o preço do produto?"))
    lista_preços.append(preço)
    if preço > 1000:
        produtos_1000 += 1
    continuar = " "
    while continuar not in 'SN':
        continuar = str(input("Adicionar mais produtos?[S/N]")).strip().upper()
    if continuar == 'N':
        break
mais_barato = (lista_produtos[lista_preços.index(min(lista_preços))])
print(f"\nO total gasto na compra foi R${fsum(lista_preços):.2f}")
print(f"{produtos_1000} produtos custaram mais de R$1000")
print(f"O produto mais barato é {mais_barato} custando R${min(lista_preços)}\n\n")


print("*" * 25)
print("nota fiscal:")
for i in range(len(lista_preços)):
    print(f"{lista_produtos[i]}-R${lista_preços[i]}")
print(f"\nTotal =R${fsum(lista_preços)}")
print("*" * 25)'''
