print('=' * 23)
print('{:^22}'.format('10 TERMOS DE PA'))
print('=' * 23)
term = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
decimo = term + (10 - 1) * raz
for c in range(term, decimo + raz, raz):
    print(c, end=' -> ')
print('ACABOU')
