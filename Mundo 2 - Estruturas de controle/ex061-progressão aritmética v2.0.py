print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao_pa = int(input('Razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo}', end=' -> ')
    termo += razao_pa
    c += 1
print('FIM!')
