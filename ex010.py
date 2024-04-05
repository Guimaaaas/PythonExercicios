num = float(input('Quanto reais você tem na carteira: R$'))
dollar = 5.06

print('\nCotação atual do dólar é {:.2f}'.format(dollar))
print('Com {:.2f} você pode comprar US${:.2f}'.format(num,num/dollar))