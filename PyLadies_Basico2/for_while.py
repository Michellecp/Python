nomes = input('Digite vários nomes separados por vírgula: ')
pessoas = nomes.split(',')
print(pessoas)
lista_peso_nome = []
lista_nome_peso = []
for nome in pessoas:
    resposta = input('Digite o peso de {}: '.format(nome))
    peso = float(resposta)
    print('Nome {}: {} kg.'.format(nome, peso))
    lista_peso_nome.append((peso, nome))
    lista_nome_peso.append((nome, peso))
print(sorted(lista_peso_nome))
print(sorted(lista_nome_peso))