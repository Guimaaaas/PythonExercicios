import datetime
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = datetime.date.today().year
    print('Ao escolher 0 é utilizado o ano atual!')
if ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
elif ano % 100 == 0:
    print('O ano de {} NÃO é bissexto!'.format(ano))
elif ano % 4 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} NÃO é bissexto!'.format(ano))
