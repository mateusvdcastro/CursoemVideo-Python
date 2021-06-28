from ex108 import moeda

p = float(input('Digite o preço: R$ '))
print(f'O dobro de R$ {moeda.moeda(p)} é R$ {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de R$ {moeda.moeda(p, "US")} é R$ {moeda.moeda(moeda.metade(p))}')  # pr mostrar q dá para mudar o R$
print(f'Aumentando em 10% temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo em 10% temos {moeda.moeda(moeda.diminuir(p, 10))}')
