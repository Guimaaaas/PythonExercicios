contador = 0
somatorio = 0
for c in range(1,501,2):
    if (c % 3) == 0:
        somatorio += c
        contador += 1
print('A soma de todos os {} valores solicitados é {}'.format(contador,somatorio))