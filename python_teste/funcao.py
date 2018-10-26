import meuprograma

pode_parar= False
lista_nomes=[]
lista_idades=[]
ano_corrente=2018

while pode_parar == False:
    nome_inf = meuprograma.pergunta_nome()
    if nome_inf == 'parar':
        pode_parar = True
    else:
        lista_nomes.append(nome_inf)
        lista_idades.append(meuprograma.pergunta_idade(ano_corrente))

print(lista_nomes)
print(lista_idades)

#zip - junta as lista
# list - coloca as informações dentro de uma lista

lista_final=list(zip(lista_nomes,lista_idades))
print(lista_final)
