print('=' * 35)
print('{:^35}'.format('BANCO CEV'))
print('=' * 35)

saque = int(input('Qual valor você quer sacar? R$'))

for nota in [50, 20, 10, 1]:
    qtd = saque // nota
    saque = saque % nota
    if qtd > 0:
        print(f'Total de {qtd} cédulas de R${nota}')
