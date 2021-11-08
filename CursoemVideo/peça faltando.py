pecas = []


def peca_faltante(Q):
    n = len(Q)
    total = (n + 1) * (n + 2) / 2
    sum_of_pecas = sum(Q)
    return total - sum_of_pecas


N = int(input("Digite o número de peças [2 a 1000]: "))

while len(pecas) < N-1:
    m = int(input("Digite as peças: "))
    if m > N or m < 0:
        print("Número inválido")
    elif m in pecas:
        print("Número já adicionado")
    else:
        pecas.append(m)

print(pecas)
miss = peca_faltante(pecas)
print(f"{miss:.0f}")

