n = str(input('Digite uma frase: ')).strip()
print(f'A letra A aparece {n.lower().count("a")}')
#    +1 para que não apareça 0º posição
print(f'A primeira letra A aparaceu na {n.find("a")+1}º posição')
#      n.rfind() para que ele começe a analisar pelo lado direito(right)
print(f'A última letra A apareceu na {n.rfind("a")+1}º posição')
