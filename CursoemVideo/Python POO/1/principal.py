from pessoa import Pessoa

p1 = Pessoa('Yan', 19)
p2 = Pessoa('Eiji', 19)
p1.outro_metodo()
p1.comer('Maçã')
p1.parar_comer()
p1.comer('Banana')
p1.parar_comer()
p1.parar_comer()
p2.falar('Animes')
p2.comer('Beterraba')
p1.falar('Games')
p2.parar_falar()

print(p1.ano_atual, end='/')
print(p2.ano_atual, end='/')
print(Pessoa.ano_atual, end='')
print()

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
