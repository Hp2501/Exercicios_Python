#Programa para Calculo de area

pl = float(input('\nLargura da parede? '))
pa = float(input('Altura da parede? '))
r = pl * pa / 2
print('A parede tem {}m² e serao necessario {:.2f}lt tinta.'.format(pl * pa, r))
