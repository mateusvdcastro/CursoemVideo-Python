c = cont = soma = maior = menor = 0
while c != 'n':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar?: [S/N]')).lower()
    cont = cont + 1
    soma = soma + n
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
média = soma/cont
print(f'Você digitou {cont} números e a média foi {média}\nO maior número é o {maior} e o menor {menor}')
