num=int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL 
[3] converter para HEXADECIMAL''')

opcao=int(input('Sua opção: '))

if opcao==1:
    num1=bin(num)
    print('{} convertido para BINARIO é igual a {}'.format(num,num1[2:]))

elif opcao==2:
    num1= oct(num)
    print('{} convertido para OCTAL é igual a {}'.format(num,num1[2:]))

elif opcao==3:
    num1= hex(num)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, num1[2:]))
else:
    print('Opção INVALIDA')

