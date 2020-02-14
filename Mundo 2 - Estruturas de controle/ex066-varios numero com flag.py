i = 1
c = 0
while i > 0:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor != 999:
        c += valor 
    else:
        print(f'A soma {i - 1} valores foi {c}!')
        break
    i += 1
