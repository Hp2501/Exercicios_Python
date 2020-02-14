print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
pa = int(input('Razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo}', end=' -> ')
    c += 1
    termo += pa
print('PAUSA')
mais_termos = int(input('Quantos termos voce quer mostrar a mais? '))
if mais_termos == 0:
    print('Fim!')
else:
    mais_termos += pa
    print(termo)
