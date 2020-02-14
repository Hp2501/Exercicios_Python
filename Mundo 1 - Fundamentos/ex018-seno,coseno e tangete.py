# Programa que le um angulo e mostra seu seno conseno e tangente

# modulo para indentificar a medida do SENO COSENO E TANGENTE
from math import radians, sin, cos, tan
ang = float(input('\nDigite o ãngulo que você deseja: '))
seno = sin(radians(ang))  # comando para o seno
cons = cos(radians(ang))  # comando para o coseno
tang = tan(radians(ang))  # comando para o tangente
print('O ãngulo de {} tem o SENO de {:.2f} '.format(ang, seno))
print('O ângulo de {} tem o COSENO de {:.2f} '.format(ang, cons))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tang))
