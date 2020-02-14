

from math import hypot#módulo para saber medidas de um triangulo e mostra o comprimento da hipotenusa
c = float(input('\nQual a medida do cateto oposto? '))
c2 = float(input('qual a medida do cateto adjacente? '))
r = hypot(c, c2)#comando para calcular o comprimento da hipotenusa
print('O comprimento da hipotenusa será {:.2f}! '.format(r))

