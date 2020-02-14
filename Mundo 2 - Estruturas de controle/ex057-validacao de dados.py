sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
if sexo == 'M' or sexo == 'F':
    print(f'O sexo {sexo} foi registrado com sucesso')
else:
    s = ' '
    while s != 'M' and s != 'F':
        dados = input('Dados inválidos. Por favor, digite seu sexo: ').strip().upper()
        s = dados
        if s == 'M' or s == 'F':
            print(f'O sexo {dados} foi registrado con sucesso')
