from datetime import date
ano = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade < 15:
    print('Classificação: INFANTIL')
elif idade > 14 and idade < 20:
    print('Classificação: JÚNIOR')
elif idade > 19 and idade < 26:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')