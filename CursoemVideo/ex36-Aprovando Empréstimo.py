valor = float(input('\033[35mQual o valor da casa desejada?: '))
salario = float(input('\033[32mQual o seu salário?: '))
ano = int(input('\033[36mEm quantos anos você quer finánciar?: '))
mensal = valor/(ano*12)
print(f'\033[33mPara pagar uma casa de \033[31m{valor:.0f}\033[m em \033[31m{ano}\033[m anos, a prestação será de \033[31m{mensal:.2f}\033[m')
if salario*0.3 >= mensal:
    print('Emprestimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')


