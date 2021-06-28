from datetime import date
a = int(input('Digite sua data de nascimento: '))
year = date.today().year
ano = year - a
print(f'O atleta tem {ano}')
if ano <= 9:
    print('MIRIM')
elif ano > 9 and ano <= 14:
    print('INFANTIL')
elif ano <= 19:
    print('JUNIOR')
elif ano <= 25:
    print('SÊNIOR')
else:
    print('MASTER')