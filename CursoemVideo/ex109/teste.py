from ex109 import moeda

p = float(input('Digite o preço: R$ '))
print(f'O dobro de R$ {moeda.moeda(p)} é R$ {moeda.dobro(p, True)}')
print(f'A metade de R$ {moeda.moeda(p, "US")} é R$ {moeda.metade(p, True)}')  # pr mostrar q dá para mudar o R$
print(f'Aumentando em 10% temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo em 13% temos {moeda.diminuir(p, 13, True)}')
