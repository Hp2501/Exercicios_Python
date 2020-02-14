i = 1
c = 0
while i > 0:
    valor = int(input('Digite um número ou 999 para parar: '))
    if valor != 999:
        c += valor 
    else:
        print(f'Você digitou {i - 1} números e a soma entre eles foi {c}')
        break
    i += 1
