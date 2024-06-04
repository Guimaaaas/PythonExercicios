print('============= LOJAS GUANABARA =============')
valor = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
forma = int(input('Sua opção: '))
if forma == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor,valor*0.9))
elif forma == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor,valor*0.95))
elif forma == 3:
    print('Sua compra de R${:.2f} será parcelado em 2x de {:.2f}.'.format(valor, valor/2))
elif forma == 4:
    parcelas = int(input('Quantas parcelas: '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, (valor * 1.2) / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor,valor*1.2))
else:
    print('Opção inválida! Tente novamente.')