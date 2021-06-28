# diferente das tuplas as listas são mutáveis
num = [1, 2, 3, 4]
num[2] = 9
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(5)
# num.remove(5)
if 10 in num:
    num.remove(10)
else:
    print('Não encontrei o valor 10')
print(num)
print(f'Esta lista tem {len(num)} elementos')
print('-'*40)

valores = []                                       # digitar valores e colocá-los dentro de listas
for v in range(0, 3):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da sua lista')

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
b = a[:]   # sem o fatiamento [:], a lista A também receberia o 8, mas dessa forma conseguimos adicionar e não relacionar as duas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
