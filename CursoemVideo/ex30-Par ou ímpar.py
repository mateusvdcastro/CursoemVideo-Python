numero = int(input('Me diga um número qualquer: '))
# divisão de resto com número par da 0 e com ímpar da 1
resultado = numero % 2
if resultado == 0:
    print(f'O número {numero} é PAR')
else:
    resultado == 1
    print(f'O número {numero} é ÍMPAR')