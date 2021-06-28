from uteis import numeros
# from uteis import fatorial,dobro,triplo    - essa forma não é recomendado pelo python, pode dar imcompatibilidade
num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O fatorial do número {num} é {fat}.')
print(f'O dobro do número {num} é {numeros.dobro(num)}')
print(f'O dobro do número {num} é {numeros.triplo(num)}')
