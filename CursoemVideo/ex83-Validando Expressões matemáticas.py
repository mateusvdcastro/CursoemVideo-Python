# solução guanabara
exp2 = str(input('Digite a expressão: '))
pilha = []
for simb in exp2:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida')

# minha solução
'''conti = contf = 0
exp = str(input('Digite uma expressão: '))
for i, v in enumerate(exp):
    if v == '(':
        conti += 1
    elif v == ')':
        contf += 1
print(contf)
print(conti)
if contf == conti:
    print('Sua expressão está válida.')
elif conti != contf:
    print('Sua expressão está inválida.')'''

# solução dos comentários
print('-='*30)
# index mostra a posição do elemento
expr1 = str(input('Digite a expressão: '))
pi = expr1.count('(')
pf = expr1.count(')')
if expr1.index(')') > expr1.index('('):
    if pi == pf:
        print('Expressão válida')
    else:
        print('Expressão é inválida')
else:
    print('Expressão inválida')

