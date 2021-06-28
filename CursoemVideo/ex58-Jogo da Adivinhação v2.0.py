tent = 0
from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número de 0 a 10.')
e = randint(0, 10)
print(e)
print('Será que você consegue advinhar qual foi?')
acertou = False
while not acertou:                      # enquanto não der outro valor diferente de False, o programa continua
    n = int(input('Qual o seu palpite?: '))
    tent += 1
    if n == e:
        acertou = True
    else:
        if n < e:
            print('Mais... Por favor digite novamente. ')
            tent += 1
        elif n > e:
            print('Menos... Por favor digite novamente. ')
            tent += 1
print(f'Acertou com {tent} tentativas parabéns!!!')
