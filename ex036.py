valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestacao = valor / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor,anos,prestacao))
if prestacao <= salario * 0.30:
    print('Empréstimo pode ser \033[32mCONCEDIDO!')
else:
    print('Emprestimo \033[31mNEGADO!')
