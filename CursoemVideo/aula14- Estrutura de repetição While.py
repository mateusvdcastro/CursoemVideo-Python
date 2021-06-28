for c in range(1, 10):                      # utilizo o for quando seu o limite(no caso 9)
    print(c)
print('Fim')

c = 1
while c < 10:                           # utilizo o while quando sei ou não sei o limite(no caso 9)
    print(c)
    c = c + 1                            #  ou   c += 1
print('Fim')

'''resposta = 'S'
while resposta == 'S':
    n = float(input('Digite um valor: '))
    resposta = str(input('Quer continuar?: [S/N]')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:                                             # quando o número digitado for 0 o programa encerra
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares')
