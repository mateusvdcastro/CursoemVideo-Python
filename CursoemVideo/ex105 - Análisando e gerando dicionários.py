def notas(*notas, sit=False):
    '''
    -> Função para análisar notas e situações de vários alunos.
    :param notas: Uma ou mais notas do aluno (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a turma.
    '''
    print('-'*30)
    dados = dict()
    dados['Total'] = len(notas)
    dados['Maior'] = max(notas)
    dados['Menor'] = min(notas)
    dados['Média'] = sum(notas)/len(notas)
    if sit:
        if dados['Média'] < 6:
            dados['Situação'] = 'Ruim'
        elif 6 <= dados['Média'] <= 7:
            dados['Situação'] = 'Bom'
        elif dados['Média'] > 7:
            dados['Situação'] = 'Ótimo'
    return dados


resp = notas(5.5, 8, 6, sit=True)  # se tirar a sit ele não exibe
print(resp)
print()
help(notas)
