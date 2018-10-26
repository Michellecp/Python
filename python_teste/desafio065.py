cont=num=soma=media=maior=menor=0
validacao='S'
while validacao not in 'N':
    num = int(input('Digite um numero:'))
    cont+=1
    soma+=num
    validacao = str(input('Deseja continuar:[S/N] ')).strip().upper()
    if cont==1:
        maior=menor=num
    else:
        if num > maior:
            maior=num
        if num < menor:
            menor=num
media=soma/cont
print('Você digitou {} numeros e a media é {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
