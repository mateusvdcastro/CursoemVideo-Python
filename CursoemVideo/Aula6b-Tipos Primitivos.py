n=(input('Digite algo: '))
print(f'O tipo primitivo desse valor é {type(n)}')
print(f'É alfabético? {(n.isalpha())}')
print(f'É Alfanúmerico? {(n.isalnum())}')
print(f'Está em Maiúsculas? {(n.isupper())}')
print(f'Está em Minúsculas? {(n.islower())}')
print(f'Está Capitalizada? {(n.istitle())}')
print(f'Tem espaços? {(n.isspace())}')
