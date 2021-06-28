n1 = float(input('PRIMEIRA NOTA: '))
n2 = float(input('SEGUNDA NOTA: '))
media = (n1+n2)/2
if media >= 6:
    print(f'Tirando {n1} e {n2}, a média do aluno é {media}\nVocê foi aprovado!!')
elif 5 <= media < 6:
    print(f'Você está de recuperação!!')
else:
    print(f'Tirando {n1} e {n2}, a média do aluno é {media}\nVocê foi REPROVADO!!')
