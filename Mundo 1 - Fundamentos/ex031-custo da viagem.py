viagem = float(input('Qual é a distância da sua viagem? '))
print('Você esta prester a começar uma viagem de {}km '.format(viagem))
if viagem <= 200:
    print('E o preco da passagem sera de R${:.2f}'.format(viagem * 0.50))
else:
    print('E o preco da passagem será de R${:.2f}'.format(viagem * 0.45))

