# solução do professor
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('Mateus')
escreva('Curso em Vídeo')
escreva('Professor Gustavo Guanabara')


# Minha solução
def escreva(text):
    print('~'*len(text))
    print(f'{text:>2}')
    print('~'*len(text))


escreva('Mateus')
escreva('Curso em Vídeo')
escreva('Professor Gustavo Guanabara')
