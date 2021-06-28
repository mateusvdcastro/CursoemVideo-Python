from random import randint,random
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO:
[2] Converter para OCTAL:
[3]'Converter para Hexadecimal: ''')
opção = int(input('Sua Opção: '))
if opção == 1:
    print(f'O número {n} convertido em BINÁRIO é {bin(n)[2:]}')
elif opção == 2:
    print(f'O número {n} convertido em OCTAL é {oct(n)[2:]}')
elif opção == 3:
    print(f'O número {n} convertido em HEXADECIMAL é {hex(n)[2:]}')
else:
    print('Está opção não existe!')
# o [2:] é para tirar a identificação de base que vem antes do nome (0o,0x,0b)