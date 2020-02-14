from random import randint
from time import sleep

cpu = randint(0, 10)
print('## Vou pensar em número de 0 a 10. Tente adivinhar! ##')
print('-=' * 27)
acertou = False
palpites = 0
print('Processando...')
sleep(2)

while not acertou:
    player = int(input('Pensei...Qual é o seu palpite? '))
    palpites += 1
    if player == cpu:
        acertou = True
    else:
        if player < cpu:
            print('Mais... Tente novamente!')
        elif player > cpu:
            print('Menos... Tente novamente!')
print(f'Acertou com {palpites} tentativas. Parabéns!')
