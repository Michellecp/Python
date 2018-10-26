sal=float(input('Qual o salario do funcionario? R$'))
if sal <= 1250 :
    sal_novo = (sal/100*15)+sal
    print('Você recebeu 15% de aumento e seu salario novo será: {:.2f}'.format(sal_novo))
else:
    sal_novo = (sal / 100 * 10) + sal
    print('Você recebeu 10% de aumento e seu salario novo será: {:.2f}'.format(sal_novo))
