from time import sleep

v1=int(input('Primeiro valor:'))
v2 =int(input('Segundo valor:'))

sair = False
while not sair:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair''')
    escolha =int(input('Qual é a sua escolha? '))
    print('--'*20)
    if escolha == 1:
        soma=v1+v2
        print('A soma entre {} e {} é {}'.format(v1, v2, soma))
    elif escolha == 2:
        mult=(v1*v2)
        print('A multiplicação entre {} e {} é {}'.format(v1,v2,mult))
    elif escolha == 3:
        if v1>v2:
            print('Entre {} e {} o maior é {}'.format(v1, v2, v1))
        elif v2>v1:
            print('Entre {} e {} o maior é {}'.format(v1,v2,v2))
        else:
            print('Os numeros são iguais!')
    elif escolha==4:
        v1 = int(input('Primeiro valor:'))
        v2 = int(input('Segundo valor:'))
    elif escolha==5:
        sair=True
        print('Finalizando...')
        sleep(20)
        print('\nFim do Program. Volte Sempre!!')
    else:
        print('Opção Invalida! Tente novamente.')
