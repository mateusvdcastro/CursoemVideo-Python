def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
            continue
        else:
            return n


def LeiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except:
            print('\033[0;31mErro! Digite um número válido!\033[m')
            continue
        else:
            return n


n = LeiaInt('Digite um número: ')
b = LeiaFloat('Digite um número quebrado: ')
print(f'Você acabou de digitar o número {n}e {b}!')
