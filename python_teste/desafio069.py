validacao=''
menor=masc=fem=0
while True:
    if validacao == 'N':
        break
    print('=='*10)
    print('CADASTRE UMA PESSOA')
    print('=='*10)
    idade=int(input('Idade:'))
    sexo=str(input('Sexo:{M/F]')).strip().upper()
    validacao=str(input('Deseja continuar?[S/N]')).strip().upper()

    if idade > 18:
        menor+=1
    elif sexo == 'M':
        masc+=1
    elif sexo == 'F' and idade < 20:
        fem+=1

print('=='*10,end='')
print('FIM DO PROGRAMA', end='')
print('=='*10)
print(f'''Total de Pessoas com mais de 18: {menor}
Ao todo temos {masc} homens cadastrados
E temos {fem} mulher com menos de 20 anos''')

