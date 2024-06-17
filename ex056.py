nomeVelho = ''
idadeVelho = 0
mulheresJovens = 0
somaIdade = 0
for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaIdade += idade
    if sexo in 'Mn' and idade > idadeVelho:
        nomeVelho = nome
        idadeVelho = idade
    elif sexo in 'Ff' and idade < 20:
        mulheresJovens += 1
print('''A média de idade do grupo é de {:.1f} anos
O homem mais velho tem {} anos e se chama {}.
Ao todo são {} mulheres com menos de 20 anos'''.format(somaIdade / 4, idadeVelho, nomeVelho, mulheresJovens))