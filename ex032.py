cores = {'limpa':'\033[m',
         'azul':'\033[0;34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m'}

import datetime
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = datetime.date.today().year
    print('Ao escolher 0 é utilizado o ano atual!')
if ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
elif ano % 100 == 0:
    print('O ano de {} {}NÃO{} é bissexto!'.format(ano, cores['vermelho'],cores['limpa']))
elif ano % 4 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} {}NÃO{} é bissexto!'.format(ano, cores['vermelho'],cores['limpa']))
