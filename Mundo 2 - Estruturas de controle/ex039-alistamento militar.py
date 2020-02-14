from datetime import date
atual = date.today().year
sexo = input('Digite se seu sexo e "M" ou "F": ').upper()
nome = input('Digite seu nome: ').strip().upper()
nasc = int(input('Ano de nascimento '))
idade = atual - nasc
print('Quem nasce em {} tem {} anos em {}'.format(nasc, idade, atual))
if sexo == 'F':
    print('Você não precisa fazer o alistamento obrigatório militar,\nPorque o alistamento só é obrigatório para os homens! ')
elif idade == 18:
    print('Você tem que se alista IMEDIATAMENTE ')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para se alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))









