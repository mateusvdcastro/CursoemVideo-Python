print('-=-'*30)
print('Analisador de Triângulos')
print('-=-'*30)
n1=float(input('Primeiro segmento: '))
n2=float(input('Segundo segmento: '))
n3=float(input('Terceiro segmento:'))
if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print(f'O triangulo existe!!')
else:
    print(f'O triângulo não existe')
