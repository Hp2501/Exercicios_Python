from datetime import date
nome = str(input('Digite o nome do aluno: ')).strip().upper()
data = int(input('Digite o ano de nascimento do aluno: '))
ano = date.today().year
idade = ano - data
if idade <= 9:
    print('O aluno {}, nascido em {}. \nQue hoje está com {} anos! \nSe enquadra na categoria MIRIM, que é de até 9 anos!. '.format(nome, data, idade))
elif idade <= 14:
    print('O aluno {} nascido em {}. \nQue hoje esta com {} anos. \nSe enquadra na categoria INFANTIL, que é de 10 até 14 anos! '.format(nome, data, idade))
elif idade <= 19:
    print('O aluno {} nascido em {}. \nQue hoje está com {} anos. \nSe enquadra na categoria JUNIOR, que é de 15 até 19 anos! '.format(nome, data, idade))
elif idade <= 25:
    print('O aluno {} nascido em {}. \nQue hoje está com {} anos. \nSe enquadra na categoria SÊNIOR, que é de 20 anos até 25 anos! '.format(nome, data, idade))
else:
    print('O aluno {} nascido em {}. \nQue hoje esta com {} anos. \nSe enquadra na categoria MASTER, que é acima dos 25 anos! '.format(nome, data, idade))
