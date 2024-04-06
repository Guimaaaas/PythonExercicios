num = float(input('Qual o salário do funcionário? R$'))
novo = num + (num*0.15)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(num,novo))