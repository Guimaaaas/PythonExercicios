cores = {'limpa':'\033[m',
         'azul':'\033[0;34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m'}

dist = float(input('Qual a distância da sua viagem: '))
print('Você está prestes a fazer uma viagem de {:.1f}Km.'.format(dist))
preco = dist * 0.50 if dist <= 200 else dist *0.45
print('E o preço da sua passagem será de {}R${:.2f}'.format(cores['verde'], preco))



'''if dist <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(dist * 0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(dist * 0.45))'''
