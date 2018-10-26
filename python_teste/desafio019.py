from random import choice
a1=str(input('Primeiro Aluno: '))
a2=str(input('Segundo aluno: '))
a3=str(input('Terceiro aluno: '))
a4=str(input('Quarto aluno: '))

lista=[a1,a2,a3,a4]

sorteio=choice(lista)

print('O aluno escolhido foi {}'.format(sorteio))