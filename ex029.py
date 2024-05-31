vel = int(input('Qual a velocidade atual do carro: '))
lim = 80
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de {}Km/h'.format(lim))
    print('Você deve pagar uma multa de RS{:.2f}!'.format(float((vel - lim)*7)))
print('Tenha um bom dia! Dirija com segurança!')
