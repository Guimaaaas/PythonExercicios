maior = 0
homens = 0
mulherMenos20 = 0
while True:
    print('--------------------------------------')
    print('CADASTRE UMA PESSOA')
    print('--------------------------------------')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    while sexo not in 'MmFf':
        print('Sexo inválido! Tente novamente')
        sexo = input('Sexo [M/F]: ')
    print('--------------------------------------')
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulherMenos20 += 1
    cont = input('Quer continuar [S/N]: ')
    while cont not in 'SsNn':
        print('Comando inválido! Tente novamente')
        cont = input('Quer continuar [S/N]: ')
    if cont in 'Nn':
        break
print(f'''Total de pessoas com mais de 18 anos: {maior}
Ao todo temos {homens} homens cadastrados
E temos {mulherMenos20} mulheres com menos de 20 anos''')
