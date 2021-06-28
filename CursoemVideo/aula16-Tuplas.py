# () tuplas são identificadas por (), mas na nova versão do Python n é mais necessário colocar
# lanche = ('Hambúrguer', 'suco') por exemplo
# Tuplas são imutáveis
# Por exemplo lanche[1] = 'Refrigerante' se isso for digitado da erro no console

lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
print(lanche)
print(lanche[2])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[2:2])

print()

print(sorted(lanche))                    # sorted() irá organizar a tupla em ordem alfabética, e para isso a transformando em lista
print(lanche)

print()

a = (2, 3, 5)                            # irá juntar uma tupla na outra
b = (5, 2, 8, 1)
c = a + b
print(c)
print(len(c))
print(c.count(5))                       # quantas vezes o número 5 aparece em c
print(c.index(8))                       # Irá mostrar em qual posição está o 8
print(c.index(2, 4))                    # Irá mostrar o 2 apartir da posição 4, uma vez que temos 2 números 2, e ele
                                        # mostra a primeira ocorrência

print()

pessoa = ('Mateus', 18, 'M', 63)
# del(pessoa[1])                     Ele não vai deletar a idade pois as tuplas são imutáveis
print(pessoa)

print()

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi para caramba!')

print()

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print()

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi para caramba!')

print()

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
