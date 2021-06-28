from ex107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}')
print(f'Aumentando em 10% temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo em 10% temos {moeda.diminuir(p, 10)}')
