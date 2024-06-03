cores = {'limpa':'\033[m',
         'azul':'\033[0;34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m'}

salario = float(input('Qual é o salário do funcionário: R$'))
if salario > 1250.00:
    novoSalario = salario * 1.10
else:
    novoSalario = salario * 1.15
print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{} agora.'.format(cores['verde'],salario,cores['limpa'], cores['verde'], novoSalario, cores['limpa']))
