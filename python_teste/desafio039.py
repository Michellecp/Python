from datetime import date

ano=int(input('Digite o ano de nascimento: '))
print('''Seu Sexo:
            [F] - Feminino
            [M] - Masculino''')
sexo=input()

atual= date.today().year
a_atual = atual - ano

print('Quem nasceu em {} tem {} anos em 2017'.format(ano, a_atual))

if sexo=='M' or sexo=='m':

    if a_atual < 18:
        print('Ainda faltam {} anos para o Alistamentos'.format(18-a_atual))
        print('Seu alistamento será em {}'.format(((18-a_atual)+atual)))
    elif a_atual >18:
        print('Você deveria ter se alistado há {}'.format(a_atual-18))
        print('Seu alistamento foi em {}'.format((18-a_atual)+atual))
    elif a_atual == 18:
        print('Você tem que se alistar IMEDIATAMENTE')

else:
    print('Você é mulher, não passará pelo alistameto Militar!!')