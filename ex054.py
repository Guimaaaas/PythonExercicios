from datetime import date

anoAtual = date.today().year
maior = 0
menor = 0
for i in range(0, 7):
    anoNasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(i+1)))
    if anoAtual - anoNasc >= 18:
        maior += 1
    else:
        menor += 1
print('''Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas menores de idade'''.format(maior,menor))
