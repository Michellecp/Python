from datetime import date

nasc=int(input('Ano de Nascimento: '))
atual=date.today().year
atual_c=atual-nasc
print('O atleta tem {}'.format((atual_c)))

if atual_c <= 9:
    print('Classificação: MIRIM')
elif atual_c < 14:
    print('Classificação: INFANTIL')
elif atual_c <= 19:
    print('Classificação: JUNIOR')
elif atual_c <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
