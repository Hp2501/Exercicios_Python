from random import randint
from time import sleep

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR [Melhor de 3]')
print('=-' * 20)

acertos_cpu = 0
acertos_usuario = 0
cont = 0
while cont < 3:
    valor = int(input('\nDigite um valor: '))
    cpu = randint(0, 10)
    print('Cpu: Estou Pensando...')
    sleep(0.5)
    total = valor + cpu

    usuario = ' '
    while usuario not in 'PI':
        usuario = str(input('Par ou Ìmpar? [P/I] ')).strip().upper()[0]
    print(f'\nVocê jogou {valor} e o computador {cpu}. Total de {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else ' DEU ÍMPAR')
    if usuario == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            acertos_usuario += 1
            cont += 1
        else:
            print('Você PERDEU!')
            acertos_cpu += 1
            cont += 1
    elif usuario == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            acertos_usuario += 1
            cont += 1
        else:
            print('Você PERDEU!')
            acertos_cpu += 1
            cont += 1

print(f'\nVocê ACERTOU {acertos_usuario} vezes!')
print(f'O computador ACERTOU {acertos_cpu} vezes!')
print('-' * 30)
if acertos_usuario > acertos_cpu:
    print('PARABÉNS. Você VENCEU a rodada!!!')
elif acertos_usuario < acertos_cpu:
    print('QUE PENA. O computador VENCEU rodada!!!')
else:
    print('OPAAA. Houve um EMPATE!')
