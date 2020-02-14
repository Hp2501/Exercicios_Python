num = int(input('\nDigite um valor: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Sua unidade é: {}'.format(u))
print('Sua Dezena é: {}'.format(d))
print('Sua Centena é: {}'.format(c))
print('Sua Milhar é: {}'.format(m))
