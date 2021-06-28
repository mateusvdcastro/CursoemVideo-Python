cont = 0
soma = 0
while True:
    n = int(input('Digite um número [ou 999 para parar]: '))
    if n == 999:                                             # a minha condição de parada se chama flag
        break
    cont += 1                                    #o contador e a soma devem vir dps do break, para que a flag seja desconsiderada
    soma += n
print(f'Você digitou {cont} números e a soma de todos eles deu {soma}')
