from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoas}° pessoa nasceu? '))
    idade = ano_atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'O total de pessoas menores de idade na lista é de {totmenor}')
print(f'O total de pessoas maiores de idade na lista é de {totmaior}')
