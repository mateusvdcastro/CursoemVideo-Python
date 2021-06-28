p = float(input('Qual o preço da compra?: '))
print('FORMAS DE PAGAMENTO:')
print('''[1] À VISTA COM DINHEIRO/CHEQUE
[2]À VISTA NO CARTÃO
[3]2x no Cartão
[4]3x ou mais no cartão''')
opcao = int(input('Qual é a opção?'))
if opcao == 1:
    n = p * 0.9
    print(f'Com essa opção você recebe 10% de desconto e o valor fica {n}R$')
elif opcao == 2:
    n1 = p * 0.95
    print(f'Com essa opção você ganha 5% de desconto e o valor fica {n1}R$')
elif opcao == 3:
    n2 = p / 2
    print(f'Com essa opção o preço é o mesmo ficando 2x de {n2}R$')
else:
    v = int(input('Em quantas vezes no cartão?: '))
    n3 = (p * 1.2)/v
    print(f'Com essa opção o preço leva 20% de juros ficando no valor de {v}x de {n3}R$')

