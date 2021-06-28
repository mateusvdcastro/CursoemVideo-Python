from datetime import date, datetime
# datetime.now().year ou usar deste modo para pegar o ano atual
anoa = date.today().year
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano no de nascimento: '))
dados['Idade'] = anoa - nasc
dados['ctps'] = int(input('Carteira de Trabalho (digite 0 se não tiver): '))
if dados['ctps'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - anoa)
print('-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
