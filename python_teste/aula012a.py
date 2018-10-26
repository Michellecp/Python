nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo' :
    print('Que nome bonito!')
elif nome == 'Pedro' or nome=='Maria' or nome=='Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claúdia Jessica Juliana':
    print('Que nome feminino lindo')
else:
    print('Seu nome é tão normal')
print('Tenha um bom dia {}!'.format(nome))