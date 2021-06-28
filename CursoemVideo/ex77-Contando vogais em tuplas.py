tupla = ('Curso', 'Video', 'Aula', 'Maquina', 'Computador', 'Ensino', 'Python', 'Programação',
         'Brasil', 'Carro', 'Camiseta')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:                           # pois cada palavra na tupla é uma lista de letras
        if letra in 'aeiou':
            print(letra, end=' ')
