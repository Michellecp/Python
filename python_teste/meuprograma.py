'''
Módulo que contém a classe Entrevista

Essa classe sera utilizada para instanciar e guardar cada Entrevista
feita pelo programa, mais as entrevistas guardadas em disco.

Os dados dessa instancia serão usados para fazer estatisticas.
'''

from datetime import date

class Entrevista():
    '''Classe Entrevista'''

    def __init__(self, nome = '', idade = 0, ano = 0):#precisa dos valores padrões
        '''Entra com os valores iniciais, Variaveis do Sistema

        nome= nome informado pelo entrevistado
        ano = ano de nascimento informado pelo entrevistado
        idade = é a idade calculada do entrevistado
        '''
        super(Entrevista, self).__init__()
        self.nome = nome
        self.idade = idade
        self.ano_inf = ano

    def pergunta_nome(self):
        '''Pergunta o nome do entrevistado. Retorna uma String.'''
        nome_ok = False
        while nome_ok == False:
            self.nome=input('Qual é o seu nome?(Digite "parar" para encerrar)')
            if self.nome:
                nome_ok = True
                if self.nome.lower() != 'parar':
                    print(f'Seu nome é {self.nome}')

        self.nome=self.nome.title()

        return self.nome

    def pergunta_idade(self):
        '''
        Pergunta o ano de nacimento e valida a idade.

        Valida o valor entre 1900 e o ano atual, através do
        date.today().year.
        Se validado calcula a idade.

        '''

        ano_atual = date.today().year
        ano_ok = False
        while ano_ok == False:
            try :
                 self.ano_inf = int(input('Ei {}, qual é o seu ano de nascimento:'.format(self.nome)))
                 ano_ok=True
            except:
                 continue
            else:
                if self.ano_inf >= 1900 and self.ano_inf<= ano_atual:
                    pass
                else:
                    ano_ok = False

        self.idade=ano_atual-self.ano_inf
        print(f'Sua idade é {self.idade}')

    def __str__(self):
        '''Retorna uma descrição amigável do objeto'''
        return '{}/{}'.format(self.nome, self.idade)

    def __repr__(self):
        '''Retorna uma descrição precisa e unica do objeto'''
        return 'input()={} input()= int({})'.format(self.nome, self.idade)