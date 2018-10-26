n1=float(input('Primeira Nota: '))
n2=float(input('Segunda Nota: '))

media=(n1+n2)/2
print('Tirando {:.1f} e {:.1f}, a média é {}'.format(n1,n2,media))

if media < 5:
    print('O Aluno esta REPROVADO')
elif media>5 and media<6.9 :
    print('O Aluno esta de RECUPERAÇÃO')
elif media>7:
    print('O Aluno esta APROVADO')