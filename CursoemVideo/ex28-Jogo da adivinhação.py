from random import randint
from time import sleep
print('-=-'*30)
print('Vou pensar em um número de 1 a 5. Tente adivinhar... ')
print('-=-'*30)
numero = int(input('Em qual número eu pensei?: '))
e = randint(0,5)
print('PROCESSANDO...')
sleep(2)
if numero == e:
    print('Parabéns você acertou!!!')
else:
    print('Você errou!!!')

# from random import choice
# lisa= [1,2,3,4,5]
# escolha = choice(lista)
# Outra maneira de fazer