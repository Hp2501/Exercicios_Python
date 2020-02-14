#Programa para calcular valor a pagar por dia e km rodado

p1 = int(input('\nDia(s) alugado(s)? '))
p2 = float(input('Kilômetros percorridos? '))
calc = (p1 * 60) + (p2 * 0.15)
print('O cliente pagara o total de R${:.2f} '.format(calc))
