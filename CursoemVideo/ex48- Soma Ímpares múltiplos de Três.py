s = 0
cont = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        print(c, end=' ')
        s += c            # += é o mesmo que    s = s + c
        cont += + 1       # += é o mesmo que    cont = cont + 1
print(f'A somatória de {cont} números é {s}')
