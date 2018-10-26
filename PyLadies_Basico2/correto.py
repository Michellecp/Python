import csv

def ler_dados():
    nomes=input('Digite varios nomes separados por virgula: ')
    pessoas= nomes.split(',')
    print(pessoas)
    lista =[]
    for nome in pessoas:
        peso = float(input('Digite o peso de {}'.format(nome)))
        altura = float(input('Digite a  altura de {}'.format(nome)))
        print('Nome {} : {} Kg {} m'.format(nome, peso, altura))
        lista.append((nome, peso,altura))
    return lista

def escrever_dados(nome_arquivo, pessoas):
    colunas = ['Nome', 'Peso', 'Altura']
    with open(teste, 'w', newline='') as csvfile:
        writer=csv.DictWriter(cvsfile, fildnames=colunas)
        writer.writeheader()
        for nome, peso, altura in pessoas:
            pessoa={}
            pessoa['Nome'] = nome
            pessoa['Peso'] = peso
            pessoa['Altura']=altura
            writer.writerow(pessoa)

pessoas = ler_dados()
escrever_dados('nome_arquivo.cvs', pessoas)
