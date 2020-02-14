casa = float(input('Digite o valor da casa: R$'))
salario = float(input(('Digite aqui seu salário: R$')))
anos = int(input('Em quantos anos pretende pagar? '))
n1 = (casa / anos) / 12
n2 = salario * 30 / 100
if n1 <= n2:
    print('O emprestimo foi APROVADO com parcelas de R${:.3f} ao mes em {} anos! '.format(n1, anos))
else:
    print('Infelizmente O empréstimo NÃO FOI APROVADO desta vez! ')

print('\nBase de Calculo e de 30% com base no valor do salário inserido.')
