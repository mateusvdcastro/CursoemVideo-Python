c = str(input('Em qual cidade você nasceu?: ')).strip()
d = c.lower()
print(d[:5] == 'santo')


#Outra forma de fazer, porém assim não olha o começo da frase, ent Maria Santo daria True mas é false, pois
# Santo está no nome
#print('santo' in c.lower())
