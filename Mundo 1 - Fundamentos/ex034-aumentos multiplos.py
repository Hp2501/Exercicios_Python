sa = float(input('Qual é o sálario do funcionário? R$'))
if sa >= 1250:
    sa = sa + (sa * 10/100)
else:
    sa = sa + (sa * 15/100)
print('O funcionário passara a receber R${:.2f} '.format(sa))






