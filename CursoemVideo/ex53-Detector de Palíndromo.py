frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()   #O split separou a frase por palavras
t = ''.join(palavra)  # O join juntou a frase tirando os espaços entre as palavras
inverso = t[::-1]
print(f'{t}')
'''inverso = ''        #É possivel fazer por fatiamento e pelos laços
for c in range(len(t) - 1, -1, -1):
    inverso += t[c]'''
print(inverso)
if t == inverso:
    print('Temos um palíndromo')
else:
    print('Não é palíndromo')

