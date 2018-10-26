import csv
lista = []

def le_dados():
    nomes = input('Digite vários nomes separados por vírgula: ')
    pessoas = nomes.split(',')
    print(pessoas)
    lista = []
    for nome in pessoas:
        peso = float(input('Digite o peso de {}: '.format(nome)))
        altura = float(input('Digite a altura de {}'.format(nome)))
        lista.append((nome, peso, altura))
        print((lista))
    return lista
print(lista)

def cria_arq(lista):
    colunas = ['nome', 'peso', 'altura']
    with open('pessoas.csv', 'w', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=colunas)
        writer.writeheader()
        for var1,var2,var3 in lista:
            
            dicionario ={}
            dicionario['nome'] = var1
            dicionario['peso'] = var2
            dicionario['altura']= var3
            print(dicionario)

            writer.writerow(dicionario)


le_dados()
cria_arq(lista)