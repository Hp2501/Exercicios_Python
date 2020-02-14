nome = str(input('Digite o nome do aluno: ')).strip().lower()
nota1 = float(input('Digite a primera nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media <= 4.9:
    print('A média do aluno {} é de {}, e está abaixo de 5.0 aluno REPROVADO!'.format(nome, media))
elif media >= 7.0:
    print('A média do aluno {} é de {}, o aluno está APROVADO! '.format(nome, media))
else:
    print('A média do aluno {} é de {}, portanto o aluno está em RECUPERAÇÃO! '.format(nome, media))
