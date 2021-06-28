from time import sleep
print('\033[1;33m@\033[m'*50)
print('Veja qual número é maior')
n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número: '))
print('...Processando...')
sleep(2)
if n1 > n2:
    print(f'O primeiro valor {n1} é maior!!')
elif n2 > n1:
    print(f'O segundo valor {n2} é maior!!')
else:
    print('Os números são iguais!!!')
print('\033[1;33m@\033[m' * 50)
