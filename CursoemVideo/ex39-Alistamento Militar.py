from datetime import date
nasc = int(input('Ano de nascimento:'))
ano = date.today().year
idade = ano - nasc
print(f'Quem nasceu no ano de {nasc} tem hoje {idade} anos')
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    a = idade-18
    b = ano - a
    print(f'Você já deveria ter se alistado a {a} anos\nSeu alistamento foi em {b}')
else:
    c = idade - 18
    d = ano - c    # Para exemplo; c = 15 - 18 = -3 anos, d = 2020-(-3)= 2023  /// Aproveitei do menos com menos para dar certo a conta
    print(f'Você irá se alistar em {d}')

