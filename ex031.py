dist = float(input('Qual a distância da sua viagem: '))
print('Você está prestes a fazer uma viagem de {:.1f}Km.'.format(dist))
preco = dist * 0.50 if dist <= 200 else dist *0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))



'''if dist <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(dist * 0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(dist * 0.45))'''
