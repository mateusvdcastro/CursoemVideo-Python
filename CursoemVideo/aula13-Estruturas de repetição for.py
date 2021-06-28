for c in range(0, 3):    #Ele conta de 0 a 2, o 3 ele ignora
    print('OI')
print('FIM')

print('='*30)

for d in range(1, 5):
    print('OI')
    print('FIM')

print('='*30)

for f in range(0, 12, 2):  #Ele irá contar de dois em dois
    print(f)

print('='*30)

for g in range(6, 0, -1): #Irá contar de trás para frente apenas com o -1
    print(g)
print('FIM')

print('='*30)

for m in range(0, 2):
    int(input('Digite um valor: '))
print('Fim')

print('='*30)

s = 0
for n in range(0, 3):
    h = int(input('Digite um valor:'))
    s += h  #OU s = s + n
print(f'O somatório dos valores é {s}')

print('='*30)

i = int(input('INÍCIO:'))
f = int(input('FIM:'))
p = int(input('PASSO:'))
for i in range(i, f+1, p):
    print(i)

