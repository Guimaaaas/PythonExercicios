somatorio = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {}º valor inteiro: '.format(c)))
    if (num % 2) == 0:
        somatorio += num
        cont += 1
print('Você informou {} números pares e a soma deles é {}'.format(cont,somatorio))