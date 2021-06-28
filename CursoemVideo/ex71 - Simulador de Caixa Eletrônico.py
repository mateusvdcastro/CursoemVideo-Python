import emoji
from time import sleep
import playsound
print('-' * 30)
print('{:^30}'.format('\033[;;1mBando FED\033[m'))
print('-' * 30)
valor = float(input('\033[33mQual valor você quer sacar?: R$ \033[m'))
total = valor
céd = 100
númerodecéd = 0
while True:
    if total >= céd:
        total -= céd
        númerodecéd += 1
    else:
        if númerodecéd > 0:
                print(f'Total de {númerodecéd} cédulas de \033[32mR${céd}\033[m')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd =5
        elif céd == 5:
            céd = 1
        númerodecéd = 0
        if total == 0:
            break
sleep(1)
print('=' * 30)
print(emoji.emojize('Obrigado e Volte Sempre! :money_with_wings:', use_aliases=True))
