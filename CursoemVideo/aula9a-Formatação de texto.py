frase = ('Curso em Vídeo')
print(frase[3:13])

frase = ('Curso em Vídeo')
print(frase[:13])

frase = ('Curso em Vídeo')
print(frase[3:])

frase = ('Curso em Vídeo')
print(frase[3:13:2])

frase = ('Curso em Vídeo')
print(frase[::2])
print()

# forma de exibir o texto inteiro
print("""A presente pandemia do novo coronavírus desenterrou os temores de muitas pessoas de fé 
com relação ao fim dos tempos. As igrejas católicas fechadas no mundo inteiro e o culto
público a Deus suspenso por tempo indeterminado remetem-nos quase de imediato à supressão
do holocausto perpétuo, tal como profetizada no livro do profeta Daniel (cf. 9, 27)""")

print()
frase = ('Curso em Vídeo')
print(frase.count('o'))

frase = ('Curso em Vídeo')
print(frase.upper().count('O'))

frase = ('  Curso em Vídeo    ')
print(len(frase))

frase = ('Curso em Vídeo')
print(len(frase.strip()))

frase = ('Curso em Vídeo')
print(frase.replace('Vídeo', 'Python'))

frase = ('Curso em Vídeo')
frase.replace('Vídeo', 'Python')
print(frase)

frase = ('Curso em Vídeo')
frase = frase.replace('Vídeo', 'Python')
print(frase)

frase = ('Curso em Vídeo')
print('Curso' in frase)

# Irá encontrar a posição em que se encontra o inicio da palavra pesquisada
frase = ('Curso em Vídeo')
print(frase.find('Vídeo'))

frase = ('Curso em Vídeo')
print(frase.split())

frase = ('Curso em Vídeo')
dividido= frase.split()
print(dividido[0])

