num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

opcao = 0
while opcao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        soma = num1 + num2
        print(f'O resultado da soma de {num1} + {num2} é igual a {soma}')
    elif opcao == 2:
        multiplicar = num1 * num2
        print(f'{num1} X {num2} é igual a {multiplicar}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior número é o {num1}')
        else:
            print(f'O maior número é o {num2}')
    elif opcao == 4:
        print('>>> Informe os valores novamente ')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Saindo...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-=' * 20)
print('Fim do programa! Volte sempre!')
