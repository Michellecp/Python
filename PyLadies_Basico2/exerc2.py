from calc_imc import imc

nomes = input('Digite vários nomes separados por vírgula: ')
 pessoas = nomes.split(',')
 print(pessoas)
 lista = []
for nome in pessoas:
    peso = float(input('Digite o peso de {}: '.format(nome))
    altura = float(input('Digite a altura de {}'.format(nome)))
    print('Nome {}: {} kg {}m'.format(nome, peso, altura))
lista_ordenada = sorted(lista)
print(lisa_ordenada)

nome_segundo_menor_imc=lista_ordenada[1][1]
print(nome_segundo_menor_imc)

penultimo_imc = lista_ordenada[-2][0]
print(avaliar_imc(penultimo_imc))