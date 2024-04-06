num = float(input('Qual é o preço do produto? R$'))
desconto = 0.05

print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}'.format(num,int(desconto*100),num-(num*desconto)))