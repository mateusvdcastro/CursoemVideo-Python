try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a/b
except (TypeError, ValueError):
    print('Tivemos um problema com os tipos de dados que você digitou. :(')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
