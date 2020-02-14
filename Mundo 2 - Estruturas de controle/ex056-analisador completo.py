somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = 0
menoridade = 0
for p in range(1, 5):
    print(f'==== {p} Pessoa ====')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        menoridade += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade} anos')
print(f'Analisando a lista o homem mais velho se chama {nomemaisvelho} que tem {maioridadehomem} anos')
print(f'Analisando a lista existem {menoridade} mulher(s) abaixo dos 20 anos')
