from time import sleep
from random import choice
print('{:-^30}'.format(' Jokempô '))
print('''\nEscolha uma opção...
\n[0] PEDRA
[1] PAPEL
[2] TESOURA''')
opcao = int(input('\nQual é a sua jogada? '))
print('JO')
sleep(0.7)
print('KEM')
sleep(0.7)
print('PÔ!!!')
print('=' * 20)
sleep(0.7)
print('(-PAPEL VENCE PEDRA)')
print('(-TESOURA VENCE PAPEL)')
print('(-PEDRA VENCE TESOURA)')
print('=' * 20)
lista = [0, 1, 2]
computador = choice(lista)
if computador == 0 and opcao == 2:
    print('O computador escolheu PEDRA')
    print('Você escolheu TESOURA')
    print('Você PERDEU! Tente novamente.')
if computador == 1 and opcao == 0:
    print('O computador escolheu PAPEL')
    print('Você escolheu PEDRA')
    print('Você PERDEU! Tente novamente.')
if computador == 2 and opcao == 1:
    print('O computador escolheu TESOURA')
    print('Você escolheu PAPEL')
    print('Você PERDEU! Tente novamente.')
if opcao == 0 and computador == 2:
    print('Você escolheu PEDRA')
    print('O computador escolheu TESOURA')
    print('Parabéns! Você GANHOU')
if opcao == 1 and computador == 0:
    print('Você escolheu PAPEL')
    print('O computador escolheu PEDRA')
    print('Parabéns! Você GANHOU')
if opcao == 2 and computador == 1:
    print('Você escolheu TESOURA')
    print('O computador escolheu PAPEL')
    print('Parabéns! Você GANHOU')
elif opcao == computador:
    print('O computador e você escolheram a mesma opçâo! HOUVE UM EMPATE.')
elif opcao >= 3:
    print('Opção invalida! TENTE NOVAMENTE.')
