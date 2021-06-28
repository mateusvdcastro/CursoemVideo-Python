from random import sample
n1=input('Primeiro nome: ')
n2=input('segundo nome: ')
n3=input('Terceiro nome: ')
n4=input('Quarto nome: ')
lista=sample([n1,n2,n3,n4],k=2)
print(f'A ordem de apresentação será {lista}')

# k=            É a quantidade de alunos que serão escolhidos dentre os outros / sampre([n1,n2,n3,n4],k=4)
#Outro comando seria o random.shuffle()
