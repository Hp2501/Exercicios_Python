from datetime import date
ano = int(input('Que ano quer analizar? Se for o ano atual, digite 0 : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(('O ano e de {} BISSXETO '.format(ano)))
else:
    print('O ano de {} Não é BISSEXTO '.format(ano))
