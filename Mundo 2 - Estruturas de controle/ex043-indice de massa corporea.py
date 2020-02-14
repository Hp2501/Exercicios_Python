print('-=' * 13)
print('Calculadora IMC')
print('-=' * 13)
peso = float(input('Qual é seu peso atual? (Kg)'))
altura = float(input('Qual sua altura? (CM'))
calc = peso / (altura ** 2)
print('O IMC dessa pessoa está em {:.1f}'.format(calc))
if calc <= 18.5:
    print('Essa pessoa está ABAIXO do peso. ')
elif calc <= 25:
    print('Essa pessoa está no peso IDEAL. ')
elif calc <= 30:
    print('Esta pessoa está com SOBREPESO. ')
elif calc <= 40:
    print('Esta pessoa está com OBESIDADE. ')
elif calc > 40:
    print('Esta pessoa está com OBESIDADE MÓRBIDA. ')
