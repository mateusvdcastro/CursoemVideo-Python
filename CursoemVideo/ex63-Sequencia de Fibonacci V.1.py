n = int(input('Quantos termos você quer exibir?: '))
t1 = 0
t2 = 1
c = 3
print(f'{t1} - {t2} - ', end='')
while c <= n:
    t3 = t1 + t2
    c = c + 1
    print(f'{t3} - ', end='')                   # t1 - t2
    t1 = t2                                     # 0 - 1 - 1 - 2 - 3 - 5 - 8
    t2 = t3                                        # t1 - t2 -t3                 #estou andando com o t1 e t2, para gerar o t3, que é a soma dos 2 últimos termos
print('FIM')