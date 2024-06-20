nomeMenor = ''
total = caro = valorMenor = 0

print('--------------------------------')
print('LOJA SUPER BARATÃO')
print('--------------------------------')
while True:
    nome = input('Nome do produto: ')
    valor = float(input('Preço: R$'))
    total += valor
    if valorMenor == 0:
        nomeMenor = nome
        valorMenor = valor
    elif valorMenor > valor:
        nomeMenor = nome
        valorMenor = valor
    if valor >= 1000:
        caro += 1
    cont = input('Quer continuar [S/N]: ')
    while cont not in 'SsNn':
        print('Comando inválido, tente novamente!')
        cont = input('Quer continuar [S/N]: ')
    if cont in 'Nn':
        break
print(f'''O total da compra foi de R${total:.2f}
Temos {caro} produtos custando mais de R$1000.00
O produto mais barato foi {nomeMenor} que custa R${valorMenor:.2f}''')