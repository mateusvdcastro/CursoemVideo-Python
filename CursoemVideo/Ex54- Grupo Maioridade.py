from datetime import date
hoje = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu?'))
    idade = hoje - ano
    if idade > 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')
