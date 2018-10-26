from datetime import date

atual = int(input('Que ano você quer analisar? Coloque 0 para o ano atual '))
if atual == 0:
    atual=date.today().year #pega o ano atual da maquina
if atual%4==0 and atual%100!=0 or atual%400==0 :
    print('O ano de {} é BISEXTO'.format(atual))
else:
    print('O ano de {} não é Bisexto'.format(atual))

