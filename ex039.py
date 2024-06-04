from datetime import date
ano = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, anoAtual))
if idade < 18:
    print('Ainda faltam {} para seu alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(anoAtual + (18 - idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(anoAtual - (idade - 18)))
else:
    print("Você tem que se alistar \033[33mIMEDIATAMENTE!")
