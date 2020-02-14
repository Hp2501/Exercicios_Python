#Programa para calcular aumento

sa = float(input('\nSalario atual do Funcionário: r$'))
sca = sa + (sa * 15/100)
print('Um funcionário com salário atual de R${:.2f}, com 15% de aumento irá passar a receber R${:.2f}'.format(sa, sca))
