from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado


# esse programa aceita numeros com vírgula ao invés de ponto, contorna esse erro
p = dado.LeiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 12, 15)
