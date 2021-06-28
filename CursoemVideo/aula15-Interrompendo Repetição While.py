n = s = 0
while True:      # While True gera um loop infinito, pois isso existe o comando Break para sair do laço
    n = int(input('Digite um número: '))
    if n == 999:                     # 999 é o meu flag, ou seja a condição de parada
        break
    s += n
print(f'A soma foi {s} \nAcabou')
