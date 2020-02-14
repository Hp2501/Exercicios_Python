import emoji
from time import sleep
print('=' * 48)
(input('PRESSIONE "ENTER" PARA INICIAR A CONTAGEM....'))
print('=' * 48)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('BUM: fireworks: \nBUM: fireworks: \nBUM: fireworks: '))
