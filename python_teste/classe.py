'''
Pergunta e calcula estatisticas de idade dos lista_entrevistado

Este código é dividido em quatro partes a seguir:
1º parte: Ler o arquivo Json
2º parte: fazendo novas perguntas
3º parte: salvando tudo no arquivo
4º parte: calculando e mostrando estatisticas
'''

import meuprograma
import statistics
import json
import pbs
convert = pbs.Command('sh')

def carrega_dados():
    '''
    Carrega as informações do arquivo Json

    Popula a lista lista_entrevistado com instancia da classe Entrevista
    com os valores que vem do arquivo Json
    '''

    global lista_entrevistado

    def pega_dados(obj):

        '''
        Cria uma instancia nova de Entrevista.

        Usa os dados vindos do json através do objeto 'obj'
        para nome, idade e ano_inf
        Retorna a instacia Entrevista()
        '''

        instancia = meuprograma.Entrevista(
            nome=obj['nome'],
            idade=obj['idade'],
            ano=obj['ano']
            )
        return instancia

    try:
        arquivo_json = open('dados.json','r') #Abre o arquivo no disco
        dados_json = json.load(arquivo_json) #Converter dicionario Json -> Python
        entrevistas = dados_json['Entrevistas']

        lista_entrevistado = [pega_dados(entrevista) for entrevista in entrevistas]

    except Exception as erro:
       print('Ocorreu um erro ao carregar ao arquivo')
       print('O erro é {}'.format(erro))

def novos_dados():
    '''
    Pergunta novos nomes e anos de nascimento.

    Enquanto o usuario não digitar "parar" ao perguntado, o nome,
    programa pergunta o ano de nascimento e calcula a idade.
    '''

    lista_entrevistado = []

    pode_parar = False
    while pode_parar == False:
        entrevistado = meuprograma.Entrevista()
        if entrevistado.pergunta_nome().lower() == 'parar':
            pode_parar = True
        else:
            try:
                entrevistado.pergunta_idade()
            except Exception as erro:
                print('Ocorreu um erro!')
                print('O tipo de erro foi {}!'.format(type(erro)))
                print('A mensagem foi {}'.format(erro))
            else:
                lista_entrevistado.append(entrevistado)


def salvar_dados():
    '''
    Salva as informações geradas em um arquivo Json.

    Converte o dicionario Python para Json e salva os dados na
    Lista lista_entrevistado.

    Cria lista no formato [{nome=obj.nome, ano=obj.ano, idade=obj.idade}]
    Transforma a lista em dicionario {"Entrevista": lista}
    '''

    lista_entrevistado =[]

    lista_salvar = [
        dict(nome=obj.nome, ano=obj.ano_inf, idade=obj.idade)
        for obj in lista_entrevistado
    ]
    dict_salvar = {"Entrevista": lista_salvar}
    dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)

    try:
        arquivo_json = open('dados.json', 'w')#Abre o arquivo e limpa
        arquivo_json.write(dict_salvar) # Escreve os dados do arquivo
        arquivo_json.close() #Fecha e salva o arquivo

    except Exception as erro:
        print('Ocorreu um erro ao salvar o arquivo')
        print('O erro é {}'.format(erro))


def calcular_dados():
    '''
    Calcula as estatisticas de idade

       1 - Mostrar a menor idade calculada
       2 - Mostra a maior idade calculada
       3 - Mostra a média de idade dos adultos
       4 - Mostrar a quantidade de nascidos por década
    '''

    #lista por compreensão
    #lista = [ < expressao para o valor > < loop > <expressao para o loop>]

    lista_entrevistado = []

    menor_idade = min([objeto.idade for objeto in lista_entrevistado])
    maior_idade = max([objeto.idade for objeto in lista_entrevistado])
    media_adulto = statistics.median_high(
        [objeto.idade for objeto in lista_entrevistado if objeto.idade>=18])

    lista_decadas=[int(objeto.ano_inf/10)*10 for objeto in lista_entrevistado]
    set_decadas = set(lista_decadas)

    # dicionario por compreensão
    # dicionario = [ <expressao para a chave>:<expressao para os valor>< loop ><expressao para o loop>]

    qtda_nascimento = {decada:lista_decadas.count(decada) for decada in set_decadas}


    print("""\nResultados:
    ---------------------------------------------
    Quantidade de Entrevistas:{}
    Menor Idade Informada: {}
    Maior Idade Informadas: {}
    Média de Idade dos Adultos Informados: {}
    """.format((len(lista_entrevistado)), menor_idade, maior_idade, media_adulto))
    print('-------------------------------------------')
    print('Nascido por décadas:')
    for decada, quantidade in qtda_nascimento.items():
        print('{}: {} nascimentos'.format(decada, quantidade))
    print('\n\n')

    resposta_ok = False

    while resposta_ok == False:
        resposta = input('Deseja mostrar os dados em um arquivo? (s/n)')
        resposta = resposta[0].lower()
        if resposta == 's' or resposta == 'n':
            resposta_ok = True

    if resposta == 's':
       sh.gedit('Dados.json')


carrega_dados()
novos_dados()
salvar_dados()
calcular_dados()
