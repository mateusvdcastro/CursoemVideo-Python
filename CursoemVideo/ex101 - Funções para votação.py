print('-'*30)


def voto(ano):
    from datetime import date                   # fazer a impotação local apenas para a def economiza muita memória
    n = date.today().year
    idade = n - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


# Programa principal
print(voto(int(input('Em que ano você nasceu?: '))))
