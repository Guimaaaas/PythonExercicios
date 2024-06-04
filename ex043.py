peso = float(input('Digite seu peso: (Kg)'))
altura = float(input('Qual a sua altura: (m)'))
imc = peso / (altura * 2)
print('O IMC dessa pessoa é de \033[0;34m{:.1f}\033[m'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso ideal!')
elif imc >= 18.5 and imc <= 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc > 25 and imc <= 30:
    print('Você está na faixa de SOBREPESO')
elif imc > 30 and imc <= 40:
    print('Você está na faixa de OBESIDADE')
else:
    print('Você está na faixa de OBESIDADE MÓRBIDA')
