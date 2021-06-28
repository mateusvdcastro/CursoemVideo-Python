from time import sleep
opção = 0
while opção != 5:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    print('''    [1] Somar
    [2] multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa''')
    opção = int(input('>>>>> Qual a sua opção?: '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma dos valores é {soma}')
    elif opção == 2:
        mult = n1*n2
        print(f'A multiplicação deu {mult}')
    elif opção == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        else:
            print(f'O maior número é {n2}')
    elif opção == 4:
        print('Digite os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Número inválido. Digite novamente!')
    print('=-='*10)
    sleep(1)
print('Fim do programa! Volte sempre.')