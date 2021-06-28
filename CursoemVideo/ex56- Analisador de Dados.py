idade = 0
maisvelho = 0
mulheres = 0
nomemaisvelho = ''
for c in range(1, 5):
    print(f'----- {c}º PESSOA -----')
    n = str(input('NOME:')).strip()
    i = int(input('IDADE: '))
    s = str(input('SEXO [F/M]:')).strip()
    idade = idade + i
    if s in 'Ff' and i < 20:
        mulheres = mulheres + 1
    if c == 1 and s in 'Mm':               #ao invez de dar .supper() caso a pessoa digite M maiusculo ou minusc, a função
        maisvelho = i                      # in 'Mm' verifica a ocorrencia das duas
        nomemaisvelho = n
    if i > maisvelho and s in 'Mm':
            maisvelho = i
            nomemaisvelho = n
média = idade/4
print(f'A média de idade do grupo é de {média} anos')
print(f'O homem mais velho tem {maisvelho} anos e se chama {nomemaisvelho}')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos')


