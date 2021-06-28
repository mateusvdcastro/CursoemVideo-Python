from math import sin, tan, cos,radians

a = float(input('Digite um ângulo: '))
print(f'O ângulo de {a} tem o SENO de {sin(radians(a)):.2f}')
print(f'O ângulo de {a} tem o COSSENO de {cos(radians(a)):.2f}')
print(f'O ângulo de {a} tem o TANGENTE de {tan(radians(a)):.2f}')
