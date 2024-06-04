cores = {'limpa':'\033[m',
         'azul':'\033[0;34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m'}

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {}'.format(nota1, nota2, media))
if media < 5:
    print('O aluno está {}REPROVADO!{}'.format(cores['vermelho'],cores['limpa']))
elif media >= 5 and media < 6.9:
    print('O aluno está em {}RECUPERAÇÃO!{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('O aluno está {}APROVADO!{}'.format(cores['verde'],cores['limpa']))
