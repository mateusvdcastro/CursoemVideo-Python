from math import sqrt, hypot

co = float(input('Quanto mede o cateto oposto?: '))
ca = float(input('Quanto mede o cateto adjacente? '))
print(f'A hipotenusa vai medir {sqrt(pow(co, 2) + pow(ca, 2)):.2f}')

# melhor jeito de fazer
print(f'A hipotenusa vai medir {hypot(co, ca):.2f}')
