
gato={'Portugues':'Gato','Ingles':'Cat','Espanhol':'Gato','Frances':'Chat','Alemão':'Katze','Italiano':'Gatto'}
for item in sorted(gato.items()):
    print(item)

gato={'Portugues':'Gato','Ingles':'Cat','Espanhol':'Gato','Frances':'Chat','Alemão':'Katze','Italiano':'Gatto'}
'''for item in sorted(gato.items(), reverse=True):
    print(item)'''

for item in sorted(gato.items()):
 if not item.endswith('ês'):
     print(gato[item])