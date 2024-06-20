print('='*30)
print('{:^30}'.format('BANCO DEV'))
print('='*30)
valor = float(input('Qual valor você quer sacar: R$'))
resto = valor
if valor >= 50:
    cinq = int(valor/50)
    resto = valor - (cinq*50)
    print(f'Total de {cinq} cédulas de R$50')
if resto >= 10:
    dez = int(resto / 10)
    resto = valor % 10
    print(f'Total de {dez} cédulas de R$10')
if resto >= 1:
    um = int(resto / 1)
    resto = valor % 1
    print(f'Total de {um} cédulas de R$1')
if resto > 0 and resto < 1:
    centavos = resto
    print(f'E {centavos*100:.0f} centavos')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
