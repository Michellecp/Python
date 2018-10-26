from datetime import date
cont_me=0
cont_ma=0
idade=0
atual=date.today().year
for c in range (0,7):
    ano=int(input('Digite o ano de nascimento: '))
    idade = atual-ano
    if ano < 21:
        cont_me+=1
    else:
        cont_ma+=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont_ma))
print('E também tivemos {} pessoas menores de idade'.format(cont_me))