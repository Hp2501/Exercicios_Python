#Programa de conversao de real para dolar

r = float(input('\nConversor de real para dólar| Digite o valor: R$'))
d = r / 4.10
e = r / 4.58
print('Com {:.2f} real(s) voce pode comprar US${:.2f} dólar(s) e €{:.2f} euro(s)'.format(r, d, e))
