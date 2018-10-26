from random import  randint
resul=''
cont=soma=0

print('-=-'*12)
print('VAMOS JOGAR PAR OU IMPAR!!')
print('-=-'*12)
while True:
    if resul=='PERDEU':
        break
    jogador=int(input('Diga um valor: '))
    validar=str(input('Par ou Impar?[P/I] ')).strip().upper()
    computador=randint(0,10)
    soma = jogador+computador
    if validar =='P':
        if soma%2 == 0:
            resul='VENCEU'
            cont+=1
        else:
            resul='PERDEU'
    elif validar =='I':
        if soma%2 != 0:
            resul='VENCEU'
            cont+=1
        else:
            resul='PERDEU'
    print(f'Você jogou {jogador} e o computador jogou {computador}. A soma deu {soma}')
    print(f'Você {resul}')
print('-=-'*12)
print(f'GAME OVER!! Você ganhou {cont} vezes.')

