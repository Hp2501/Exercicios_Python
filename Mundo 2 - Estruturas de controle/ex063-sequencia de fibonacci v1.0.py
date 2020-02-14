print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
seq = int(input('Quantos termos você quer mostrar? '))
 
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end=' -> ')
i = 3
while i <= seq:
    t3 = t1 + t2
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
    i += 1
print('FIM!')
