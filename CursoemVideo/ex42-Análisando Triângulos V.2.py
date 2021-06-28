s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo Segmento: '))
s3 = int(input('Terceiro segmento:'))
if s1 < s2+s3 and s2 < s1+s3 and s3 < s2+s1:
    exis = 'PODEM FORMAR'
    if s1 == s2 == s3:
        print(f'Os seguimentos {exis} um triângulo Equilátero!')
    elif s1 != s2 != s3 != s1:              #No != é necessário diferenciar em pares, o python não faz a sequencia como para o ==
        print(f'Os seguimentos {exis} um triângulo Escaleno')
    else:
        print('Os seguimentos PODEM FORMAR um triângulo Isósceles')
else:
    print('Não pode formar um triângulo!')

