soma=0
nome_ma=''
maior=0
cont=0
for p in range (1,5):
    print('--'*5,'{}° PESSOA'.format(p),'--'*5)
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ').upper())

    soma+=idade

    if sexo == 'M':
        if p == 1:
            maior = idade
            nome_ma=nome
        else:
            if idade > maior:
                 maior=idade
                 nome_ma=nome
    elif sexo == 'F':
        if idade < 20:
            cont+=1

media=(soma/4)

print('A média das idades do grupo é {} anos'.format(media))
print('O Homem mais velho tem {} e se chama {}'.format(maior, nome_ma))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont))

