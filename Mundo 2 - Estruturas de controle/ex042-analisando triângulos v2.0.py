l1 = float(input('Primeiro segmento '))
l2 = float(input('Segundo segmento '))
l3 = float(input('Terceiro segmento '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Os valores formam SIM um triângulo', end='')
    if l1 == l2 == l3:
        print(' EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print(' ESCALENO')
    else:
        print(' ISÓCELES')
else:
    print('Os valores NÃO formam um triângulo! ')
