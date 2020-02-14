carro = float(input('Qual a velocidade atual do carro? '))
if carro > 80:
    print('MULTADO! você excedeu o limite permitido que e de 80km/h')
    multa = (carro-80) * 7
    print('Você deve pagar uma multa de {}'.format(multa))
print('Tenha um bom dia! Dirija com SEGURANÇA! ')
