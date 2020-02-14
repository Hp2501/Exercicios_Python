from random import randint
from time import sleep
computador = randint(0, 5)  # faz o computador pensar
print('-=-' * 18)
print('Vou pensar em número entre 0 e 5. Tente adinvinhar...')
print('-=-' * 18)
jogador = int(input('Em que número eu pensei? '))# jogador tenta adinvinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! você conseguiu vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
