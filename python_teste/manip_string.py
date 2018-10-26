'''
Lista
É sempre utilizada para armazenar e mostrar
um tipo de dado especifico. Ex: Idade = [10,15,20]
'''
lista = [1,2,3,4]
print(lista)

'''
Tupla
É utilizada para armazenar e mostrar conteudos heterogenios. 
Ex: Dados = (1986, 31, 1990, 18)
'''
tupla = (1,2,3,4)
print(tupla)

total = [lista, tupla]
print(total)

'''
Dicionario:
Sintaxe (key:value)
Permite alterações, recuperação de dados
'''
dic = {"ano":1986, "idade":31, "ano":1990, "idade":18}
dic.update(nome='Rafael')
print(dic)

juros = [1,2,2,3,4,2,5]
print(set(juros)) #comando set imprime os numeros sem repetir