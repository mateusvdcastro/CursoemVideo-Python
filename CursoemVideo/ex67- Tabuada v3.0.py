while True:
    n = int(input('A tabuada de qual número você quer exibir?: '))
    print('-=' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-=' * 20)
print('Programa Encerrado!')
