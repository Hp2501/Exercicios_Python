
while True:
    print('-' * 50)
    num = int(input('Quer ver a tabuada de que valor ou "0" para SAIR? '))
    operacao = str(input('Digite a operação + - / *: '))
    print('-' * 50)

    if num == 0:
        print('Saindo...')
        break
    elif num < 0:
        print('Os números deverão ser positivos')
    elif operacao.isnumeric():
        print('Erro. Operadores são [+, -, /, *]!')
    elif operacao == "+":
        for c in range(1, 11):
            adicao = num + c
            print(f'{num} + {c} = {adicao}')
    elif operacao == "-":
        for c in range(1, 11):
            subtracao = num - c
            print(f'{num} - {c} = {subtracao}')
    elif operacao == "/":
        for c in range(1, 11):
            divisao = num / c
            print(f'{num} / {c} = {divisao:.2f}')
    elif operacao == "*":
        for c in range(1, 11):
            multiplicacao = num * c
            print(f'{num} * {c} = {multiplicacao}')
    else:
        print('Erro. Operadores são +, -, /, *')
