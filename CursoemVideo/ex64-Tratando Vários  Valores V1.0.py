n = 0                      # tambem pode escrever n = soma = 0
cont = -1
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont = cont + 1
    soma = soma + n
nf = soma - 999
print(f'Você digitou {cont} números e a soma é {nf}')
print('=-'*30)

                                                                   #outra forma de fazer
n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont = cont + 1
    soma = soma + n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma é {soma}')
